#sfdc.py

import textwrap
from typing import Optional

# --- Language Definitions ---
# (Keep this updated with accurate translations and terms)
# Assume lang_terms dictionary is defined globally here as previously provided...
lang_terms = {
    "Japanese": {
        "error_not_found": "提供されたJSONファイルに該当する企業「{company_name}」の有効なデータ（アカウント情報または関連する取引情報）が見つかりません。JSONファイルの内容を確認するか、正確な企業名（JSON内の 'Name' または 'CT_NameAbbreviation__c' と完全に一致する）を指定してください。",
        "error_json_format": "提供されたファイルは有効なJSON形式ではないか、必須のキー（'accounts', 'opportunities'）が欠落しています。",
        "error_title": "エラー",
        "no_won_deals_found": "指定された期間内に分析対象の受注済み取引（IsWon = true）が見つかりませんでした。分析はアカウント情報および全取引タイプ（受注、失注、進行中）に基づいて行われます。",
        "report_title": "【{context_company_name}内部向け】 {company_name} 取引データ戦略分析レポート",
        "exec_summary": "0. エグゼクティブサマリー（{context_company_name}向け）",
        "trend_analysis": "1. 主要受注実績 推移分析",
        "annual_revenue": "年間総受注金額",
        "annual_deal_count": "年間総受注件数",
        "avg_deal_size": "平均受注単価（年間）",
        "segment_analysis": "2. 受注セグメント分析",
        "sbu_division": "2.1 関連事業領域（アカウント情報ベース）",
        "service_product": "2.2 サービス・商材区分（取引の構造化データおよび案件名・タグからの推測）",
        "dx_strategic": "2.3 DX・戦略領域（取引の構造化データおよび案件名・タグからの推測）",
        "deal_characteristics": "3. 受注案件 特性分析",
        "avg_lead_time": "平均リードタイム（受注案件：クローズ日 - 作成日）",
        "deal_size_distribution": "受注案件規模 分布",
        "whitespace_analysis": "4. ホワイトスペース分析 / 未開拓ポテンシャル（{context_company_name}視点）",
        "client_profile_context": "クライアントプロファイル・関心領域（アカウント情報・タグ）",
        "comparison_won_deals": "受注実績との比較",
        "identified_whitespace": "特定されたホワイトスペース（{context_company_name}の潜在的機会）",
        "strategic_recommendations": "5. 戦略的考察・推奨事項（{context_company_name}向け）",
        "strengths_leverage": "活用すべき強み（既存受注領域）",
        "focus_development": "注力・開発すべき領域（トレンド・ギャップ・ホワイトスペース）",
        "quick_wins": "短期的な機会",
        "efficiency_process": "営業プロセス効率化のヒント",
        "overall_posture": "全体的な戦略的位置づけ",
        "visualization_suggestions": "6. 推奨される可視化（内部報告用）",
        "risks_mitigation": "7. {context_company_name}にとってのリスクと軽減策",
        "based_on_general_knowledge": "(※市場の一般的知識および提供データに基づく考察)",
        "unit_deals": "件",
        "unit_currency": "円", # Assuming JPY
        "unit_days": "日",
        "year": "年度",
        "data_quality_limitations": "データ品質/分析の限界",
        "derived_from_close_date": " (CloseDateから導出)"
    },
    "English": {
        "error_not_found": "Cannot find valid data (Account Information or related Opportunities) for the specified company '{company_name}' in the provided JSON file. Please check the JSON content or provide the correct company name (must exactly match 'Name' or 'CT_NameAbbreviation__c' in the JSON).",
        "error_json_format": "The provided file is not valid JSON or is missing required keys ('accounts', 'opportunities').",
        "error_title": "Error",
        "no_won_deals_found": "No completed ('Won' = true) deals were found for analysis within the specified period. Analysis will be based on Account Information and all opportunity types (won, lost, open).",
        "report_title": "[Internal {context_company_name} Report] {company_name} Transaction Data Strategic Analysis",
        "exec_summary": "0. Executive Summary (for {context_company_name})",
        "trend_analysis": "1. Key Won Deal Trend Analysis",
        "annual_revenue": "Total Annual Won Revenue",
        "annual_deal_count": "Total Annual Won Deal Count",
        "avg_deal_size": "Average Annual Won Deal Size",
        "segment_analysis": "2. Won Deal Segment Analysis",
        "sbu_division": "2.1 Related Business Areas (Based on Account Info)",
        "service_product": "2.2 Service/Product Categories (Inferred from Structured Opportunity Data, Deal Names & Tags)",
        "dx_strategic": "2.3 DX/Strategic Areas (Inferred from Structured Opportunity Data, Deal Names & Tags)",
        "deal_characteristics": "3. Won Deal Characteristics Analysis",
        "avg_lead_time": "Average Lead Time (Won Deals: Close Date - Create Date)",
        "deal_size_distribution": "Won Deal Size Distribution",
        "whitespace_analysis": "4. White Space Analysis / Untapped Potential (from {context_company_name}'s Perspective)",
        "client_profile_context": "Client Profile & Interest Areas (Account Info & Tags)",
        "comparison_won_deals": "Comparison with Won Deal History",
        "identified_whitespace": "Identified White Space (Potential {context_company_name} Opportunities)",
        "strategic_recommendations": "5. Strategic Implications & Recommendations (for {context_company_name})",
        "strengths_leverage": "Strengths to Leverage (Existing Won Areas)",
        "focus_development": "Areas for Focus/Development (Trends, Gaps, White Space)",
        "quick_wins": "Potential Quick Wins",
        "efficiency_process": "Sales Process Efficiency Insights",
        "overall_posture": "Overall Strategic Posture Recommendation",
        "visualization_suggestions": "6. Recommended Visualizations (for Internal Reporting)",
        "risks_mitigation": "7. Risks & Mitigation Strategies (for {context_company_name})",
        "based_on_general_knowledge": "(Note: Observation based on general market knowledge and provided data)",
        "unit_deals": "deals",
        "unit_currency": "JPY", # Assuming JPY
        "unit_days": "days",
        "year": "FY",
        "data_quality_limitations": "Data Quality/Analysis Limitations",
        "derived_from_close_date": " (Derived from CloseDate)"
    }
}


# --- NESIC Context ---
# Assume NESIC_CAPABILITIES_CONTEXT is defined globally here as previously provided...
NESIC_CAPABILITIES_CONTEXT = textwrap.dedent("""\
    **NESIC Capabilities & Strategic Context (Reference for Analysis):**

    *   **Core Business Domains (What We Do):**
        *   **Digital Transformation (DX) Enablement:** Partnering with clients from strategic DX consulting and roadmap design through to complex implementation and ongoing optimization, focusing on solving core business challenges and driving innovation.
        *   **Advanced System Integration (SI):** Expertise in architecting, building, testing, and integrating sophisticated, mission-critical IT systems, ensuring seamless operation within complex multi-vendor environments. Focus on reliability and future-readiness.
        *   **Next-Generation Network Solutions:** Designing, deploying, securing, and managing robust network infrastructures (LAN, WAN, Wireless, 5G/Local 5G, SD-WAN). Delivering high-performance, secure connectivity for both enterprise and carrier-grade requirements.
        *   **Comprehensive Cybersecurity Services:** Providing end-to-end security solutions: strategic consulting, risk/vulnerability assessments, advanced Security Operations Center (SOC) services, Managed Security Service Provider (MSSP) offerings, threat detection/response, and compliance support.
        *   **Strategic Cloud Services:** Enabling multi-cloud adoption (AWS, Azure, GCP, OCI+) through expert migration planning and execution, secure cloud infrastructure management, performance/cost optimization, and hybrid/private cloud integration.
        *   **Intelligent Managed Services & BPO:** Delivering high-quality IT infrastructure operation, 24/7 proactive monitoring & management, service desk support, and IT-related Business Process Outsourcing to enhance client operational efficiency, reduce TCO, and ensure service continuity.
        *   **Modern Collaboration & Communication Platforms:** Implementing and managing unified communications (UC), advanced video conferencing systems, AI-enhanced contact center solutions, and digital workplace tools to boost productivity and user experience.
        *   **Applied IoT & Data Analytics:** Designing and implementing IoT solutions for data collection/integration, providing data visualization and analytics services, often leveraging advanced AI/ML capabilities from the NEC Group to unlock business insights.
        *   **Converged Physical Security & Facility Management:** Integrating IT infrastructure with physical security systems (biometrics, surveillance, access control) and smart building/facility management solutions for enhanced safety and efficiency.

    *   **NESIC's Core Value Proposition & Strategic Approach (How We Succeed):**
        *   **Co-Creation Partnership:** We prioritize understanding client challenges deeply and collaborating closely to design and deliver the *optimal* solution, acting as a long-term strategic partner.
        *   **Leveraging NEC Group Strengths:** We uniquely integrate cutting-edge technologies (AI, biometrics, 5G/6G R&D, advanced analytics) and the broad solution portfolio of the NEC Corporation to deliver innovative and differentiated outcomes.
        *   **Ensuring Mission-Critical Reliability:** Decades of proven experience delivering and managing large-scale, complex systems for demanding clients, ensuring operational stability and resilience.
        *   **End-to-End Service Lifecycle:** Providing comprehensive support across the entire lifecycle, from initial consultation and design to implementation, management, and continuous improvement.
        *   **Vendor-Agnostic Integration Expertise:** Skillfully integrating best-of-breed solutions from a wide range of technology partners while ensuring interoperability and avoiding vendor lock-in where appropriate.

    *   **Key Differentiators (Why Choose NESIC):**
        *   **NEC Group Technology Access:** Unique ability to incorporate world-class NEC R&D and specialized technologies.
        *   **Proven SI Track Record:** Unmatched experience in delivering complex, large-scale projects within the Japanese market.
        *   **Deep Networking & Security DNA:** Core technical leadership and heritage in designing and securing critical networks.
        *   **Nationwide Delivery & Support:** Robust, skilled service infrastructure across Japan for reliable installation, maintenance, and operational support.
        *   **Client-Centric Flexibility:** Combining structured methodologies with the agility to tailor solutions and engagement models to specific client needs.

    *   **Primary Target Segments:** Large Enterprises, Government Agencies & Public Sector Organizations, Telecommunications Carriers, Critical Social Infrastructure Providers.

    **(Note for AI Strategist:** Use this context to identify how NESIC's specific capabilities, approach, and differentiators can best address the target company's identified needs, challenges, and strategic initiatives from the provided JSON data. Frame opportunities by highlighting NESIC's unique value.)
""")

# --- Instruction Blocks Specific to JSON Analysis ---
# Assume BASE_FORMATTING_INSTRUCTIONS_JSON is defined globally here as previously updated...
BASE_FORMATTING_INSTRUCTIONS_JSON = textwrap.dedent("""\
    **Output Format & Quality Requirements:**

    *   **Direct Start & No Conversational Text:** Begin the response *directly* with the report title (`# {terms['report_title']}`). Absolutely no introductory or concluding remarks outside the defined structure.
    *   **Strict Markdown Formatting:** Use valid and consistent Markdown throughout. Adhere precisely to the heading levels (`#`, `##`, `###`) specified in the REQUIRED OUTPUT STRUCTURE. Use bullets (`*` or `-`) for lists, maintaining logical indentation.
    *   **Tables (Clarity Emphasis):** Use perfectly formatted Markdown tables for trends and segment breakdowns where requested.
        *   Ensure headers are descriptive and clearly labeled (e.g., specifying the metric and unit).
        *   Ensure data alignment is logical (numbers right-aligned where possible using spaces for readability in the raw Markdown).
        *   Verify column counts match precisely on every row (header, separator, data).
        *   Use start and end pipes `|` on every row.
        *   Example Structure:
            ```markdown
            | {terms['year']} | {terms['annual_revenue']} ({terms['unit_currency']}) | {terms['annual_deal_count']} ({terms['unit_deals']}) |
            |--------|----------------------------------------|------------------------------------|
            | FY2022 |                              1,234,567 |                                 15 |
            | FY2023 |                              2,345,678 |                                 20 |
            ```
    *   **Conciseness & Analytical Depth:** Be specific, quantitative where possible, and analytical. Avoid jargon but use appropriate business terms ({context_company_name} context). Ensure clear topic sentences for paragraphs. Focus on extracting *strategic insights*, not just listing data.
    *   **Data Formatting Consistency:** Use appropriate thousands separators for numbers per the target language: **{language}**. Always specify the currency unit (`{terms['unit_currency']}`) for monetary values. Format periods consistently (e.g., YYYY {terms['year']} QX or specific date ranges). Use specified units (`{terms['unit_deals']}`, `{terms['unit_days']}`) consistently and clearly in table headers or alongside metrics.
    *   **Tone:** Professional, analytical, objective, and **strategically focused from the perspective of {context_company_name}**.
    """)
# Assume HANDLING_MISSING_INFO_INSTRUCTION_JSON is defined globally here as previously updated...
HANDLING_MISSING_INFO_INSTRUCTION_JSON = textwrap.dedent("""\
    **Handling Missing, Null, or Invalid Data in JSON Analysis:**

    *   **Basis:** All analysis MUST stem from the provided JSON data for `{company_name}`.
    *   **"No Won Deals" Scenario:** If no opportunities linked to `{company_name}` have `IsWon == true` (and potentially `Amount > 0` for revenue-based analysis), follow the specific instructions outlined in the `WON_DEAL_FILTERING_LOGIC` section (state the finding, omit quantitative analysis dependent on 'Won' deals, proceed with qualitative analysis based on *all* opportunities and account info).
    *   **Missing Categories within Segments:** If, *after* filtering for `IsWon == true` (where applicable), data for a specific *parsed* category (e.g., a Service/Product inferred from Opportunity Name or tags) results in zero revenue or zero deals, **silently omit only that specific category's line item or bullet point** from the relevant list in Section 2. Do *not* state 'N/A' or 'Zero'.
    *   **Handling Null/Missing/Invalid Fields within Records:**
        *   **`Amount`:** If `Amount` is null, non-numeric, or missing for a specific opportunity record, treat it as `0` for aggregation purposes (e.g., total revenue calculation) *after* applying relevant filters (like `IsWon == true`). **Such records MUST be excluded from average deal size calculations.** Deals with a valid `Amount` of `0.0` should also be excluded from average deal size calculation but included in deal counts and total revenue (as 0).
        *   **`CloseDate`, `CreatedDate`:** If either `CloseDate` or `CreatedDate` is null, invalid, or missing for a specific opportunity, that record **MUST be excluded** from any lead time calculation (Section 3). It can still be used for other analyses like name parsing or revenue aggregation if `Amount` is valid.
        *   **Fiscal Period Derivation:** Use `FiscalYear` and `FiscalQuarter` if present, valid, and consistently populated. If not, derive from `CloseDate`. Append "{terms['derived_from_close_date']}" to the fiscal period if derived. If `CloseDate` is also invalid, that record cannot be assigned to a fiscal period for trend analysis (Section 1).
        *   **Tag Fields (e.g., `CT_f_scenarios__c`, `sci_ttag_trends__c`):** These are often strings containing multiple values separated by commas or semicolons. **Split these strings into individual items/tags for analysis.** If a tag field is null or empty, it simply means no tags of that type are available for that record.
        *   **Other Fields:** If fields used for qualitative parsing (like `Name` or tags) are missing or null, that record cannot contribute to that specific qualitative analysis but might still be valid for quantitative metrics if `Amount`, dates, etc., are present.
    *   **Do NOT Omit Sections:** Do *not* omit entire section headings (e.g., `### 2.2 ...`) if *other* categories or data points within that section *are* valid and derivable from the JSON source.
    *   **No Placeholders for Missing Data:** Absolutely **do NOT** state '該当なし', 'N/A', '不明', 'Not Found', 'Data unavailable', or use placeholders like 'XXX {terms['unit_currency']}' *for missing data points or categories*. Only present information verifiable and calculable from the valid portions of the JSON data. If a required calculation (like Avg Lead Time) cannot be performed due to lack of 'Won' deals *or* lack of valid date fields in those deals, state the reason clearly but briefly (e.g., "{terms['no_won_deals_found']}" or "Insufficient valid date data for lead time calculation on Won deals.").
    *   **Data Quality Summary:** If significant data quality issues are encountered (e.g., >20% of 'Won' deals missing `Amount` or critical dates, pervasive vague opportunity names hindering segmentation), include a brief "Data Quality/Analysis Limitations" subsection in the Executive Summary.
    """)
# Assume JSON_DATA_PROCESSING_INSTRUCTIONS is defined globally here as previously updated...
JSON_DATA_PROCESSING_INSTRUCTIONS = textwrap.dedent("""\
    **JSON Data Processing & Field Mapping (MANDATORY):**

    *   **Input:** A single `.txt` file containing JSON with `accounts` (list) and `opportunities` (list) keys. Validate this basic structure first. If invalid, trigger `{terms['error_json_format']}`.
    *   **Account Identification:**
        1.  The `{company_name}` provided to the script **must exactly match** the value in `accounts[*].Name` or `accounts[*].CT_NameAbbreviation__c` within the JSON. Perform a case-sensitive, exact match after trimming leading/trailing whitespace from both the input `{company_name}` and the JSON field values.
        2.  Iterate through the `accounts` list. If only one account object exists, assume it's the target if its name fields are reasonably close to `{company_name}` (but prioritize exact match if multiple accounts exist).
        3.  Extract the `Id` from this matching account object.
        4.  If no matching account object is found after checking all accounts, trigger the `{terms['error_not_found']}` error.
    *   **Opportunity Filtering:**
        1. Filter the `opportunities` list to retain only objects where `AccountId` matches the Account `Id` identified above.
        2. If this results in an empty list (no opportunities linked to the account), the analysis will be very limited. Proceed with account-level information for Sections 2.1 and 4, but state that no opportunity data is available for other sections.
    *   **Field Mapping & Interpretation (Use these paths/methods; handle potential nulls/errors gracefully per `HANDLING_MISSING_INFO_INSTRUCTION_JSON`):**
        *   **Client Info (Account Level - Primarily for Context):** `accounts[0].Name`, `accounts[0].Id`, `accounts[0].CT_IndustryName__c` (Industry), `accounts[0].CT_MarketSegmentName__c` (Market Segment).
            *   **Multi-Value String Tags (Account):** These fields are CRITICAL for context and white space. They are often strings containing multiple values separated by commas and/or semicolons. **Split these strings into individual items/tags for analysis:**
                *   `accounts[0].sci_ttag_trends__c` (Trends Tags)
                *   `accounts[0].sci_ttag_businessAndServices__c` (Business Tags)
                *   `accounts[0].sci_ttag_adoptedItServiceCategory__c` (Tech Categories Used)
                *   `accounts[0].sci_ttag_services__c` (Specific Tech Services Used - may indicate competitor presence or existing {context_company_name} services)
                *   `accounts[0].CT_f_scenarios__c` (Client Scenarios/Needs Tags)
                *   `accounts[0].CT_f_service_categories__c` (Client's Service Categories)
                *   `accounts[0].CT_f_services__c` (Client's Specific Services)
        *   **Opportunity Info (Deal Level):**
            *   `Opportunity ID`: Use `opportunities[*].CT_ItemNumber__c` if available and unique, otherwise `opportunities[*].Id` or `CT_SFId__c`.
            *   `Revenue/Amount`: `opportunities[*].Amount`. Interpret as {terms['unit_currency']}. Handle null/non-numeric as 0 for totals, exclude from averages.
            *   `Is Won`: `opportunities[*].IsWon` (boolean `true`/`false`). CRITICAL filter.
            *   `Fiscal Period`: Use `opportunities[*].FiscalYear` and `opportunities[*].FiscalQuarter` if present and valid. If not, derive from `opportunities[*].CloseDate` (e.g., fiscal year ending March 31st: Q1 Apr-Jun, Q2 Jul-Sep, Q3 Oct-Dec, Q4 Jan-Mar). Append "{terms['derived_from_close_date']}" if derived.
            *   `Created Date`: `opportunities[*].CreatedDate`. Must be a valid date format.
            *   `Close Date`: `opportunities[*].CloseDate`. Must be a valid date format.
            *   `Opportunity Name`: `opportunities[*].Name`.
            *   `Stage Name`: `opportunities[*].StageName`.
            *   `Approach Type`: `opportunities[*].CT_Approach_Type__c`. (Potentially useful for segmentation).
            *   `Record Type`: `opportunities[*].RecordTypeName__c`. (Potentially useful for segmentation).
            *   **Multi-Value String Tags (Opportunity):** Similar to account tags, split these if used:
                *   `opportunities[*].sci_ttag_adoptedItServiceCategory__c`
                *   `opportunities[*].sci_ttag_businessAndServiceDetails__c`
    *   **Qualitative Comments:** Fields like `Opportunity.Description` or `CT_OpportunityProgressStatusBC__c` are generally **not** for deep semantic analysis with this prompt. They can be used for keyword spotting if a specific, simple keyword is relevant and if explicitly instructed for a very narrow purpose. Do not attempt to summarize or understand complex nuances from these free-text fields.
    """)
# Assume WON_DEAL_FILTERING_LOGIC is defined globally here as previously updated...
WON_DEAL_FILTERING_LOGIC = textwrap.dedent("""\
    **"Won Deal" Filtering Logic & Contextualization (Mandatory):**

    1.  **Create "Won Deal" Subset:** From the filtered opportunities relevant to `{company_name}`, create a specific subset containing only those where `IsWon == true`. For revenue-based metrics (Total Revenue, Average Deal Size), further ensure `Amount` is a valid number (treat null/non-numeric `Amount` as not contributing to these specific metrics, effectively filtering them out for averages, or as 0 for totals).
    2.  **Quantitative Analysis Basis:** ALL quantitative analyses (Total/Annual Revenue, Deal Counts, Averages, Lead Time in Sections 1, 2.2, 2.3, 3) **MUST** be performed exclusively on this 'Won Deal' subset, considering only records with valid data for the specific calculation (per `HANDLING_MISSING_INFO_INSTRUCTION_JSON`). Explicitly state this basis (e.g., "Analysis based on deals where IsWon = true").
    3.  **"No Won Deals" Scenario:** If the 'Won Deal' subset is empty (or contains no deals with valid positive `Amount` for revenue metrics):
        *   **State Clearly:** Report `{terms['no_won_deals_found']}` prominently in the Executive Summary (Section 0) and Trend Analysis (Section 1).
        *   **Omit Quantitative Metrics:** Do NOT calculate or display Total/Annual Revenue, Deal Counts, Average Deal Size, or Average Lead Time based on 'Won' deals. Remove or comment out these specific metrics/tables in Sections 0, 1, 3. State clearly why they are omitted (lack of 'Won' deals or valid Amount data in Won deals).
        *   **Adapt Qualitative Analysis:** Sections 2 (Segments), 4 (White Space), and 5 (Recommendations) MUST shift to a qualitative focus. Analyze patterns based on parsing names/tags/other fields from *all* opportunity types (won, lost, open) linked to the account, combined with Account-level information. Clearly state this limitation: "Due to the absence of 'Won' deals with valid revenue data in the provided records, the following segment and strategic analysis is qualitative, based on all opportunity types and account profile information."
    4.  **Context from All Deals (Even if Won Deals Exist):**
        *   **Enhance Qualitative Insights:** Even when 'Won' deals exist and form the basis for quantitative analysis, **use the full set of opportunities (won, lost, open)** to provide broader qualitative context. For example:
            *   In Section 2.1 (SBU/Account Context), briefly mention themes appearing frequently across *all* opportunity names/types/tags to understand the full scope of engagement attempts.
            *   In Section 5 (Recommendations), consider patterns in lost deals (if `StageName` or `CT_LostReason__c`/`CT_LostType__c` suggest reasons) or frequently proposed but unclosed deals when suggesting areas for focus or process improvement.
        *   **Clarity:** Clearly distinguish between analysis based *only* on 'Won' deals versus insights derived from the broader set of opportunities.
    """)
# Assume NESIC_PERSPECTIVE_INSTRUCTION is defined globally here as previously provided...
NESIC_PERSPECTIVE_INSTRUCTION = textwrap.dedent("""\
    **{context_company_name} Perspective Integration (CRITICAL):**

    *   **Viewpoint:** Frame **ALL** analysis, observations, identified opportunities, risks, and recommendations explicitly from the perspective of **{context_company_name}**. The central question is: "What does this data tell *us* ({context_company_name}) about how to strategically engage and grow our business with {company_name}?"
    *   **Capability Mapping:** Actively connect findings from the JSON data (trends, segments, client needs inferred from deal names/account tags) to specific **{context_company_name}** capabilities, strengths, and differentiators (as listed in the `NESIC_CAPABILITIES_CONTEXT`).
    *   **Value Proposition:** Articulate the potential value {context_company_name} can bring based on the analysis (e.g., "The prevalence of [X type] deals suggests NESIC's strength in [Y capability] is well-received and can be further leveraged.").
    """)
# Assume SEGMENTATION_INSTRUCTION is defined globally here as previously updated...
SEGMENTATION_INSTRUCTION = textwrap.dedent("""\
    **Segmentation Analysis Guidance (Sections 2.2 & 2.3):**

    *   **Primary Method (Structured Tags):**
        1.  For categorizing deals, **FIRST prioritize using structured tag fields from the Opportunity records** if they are present, populated, and relevant. These are likely more reliable than inferring from names. Examples:
            *   `opportunities[*].CT_Approach_Type__c` (e.g., "リテンション商談", "上流アプローチ")
            *   `opportunities[*].RecordTypeName__c` (e.g., "CT_一般取引")
            *   Opportunity-level `sci_ttag_adoptedItServiceCategory__c`, `sci_ttag_businessAndServiceDetails__c` (split comma/semicolon-separated strings into individual tags).
        2.  Group deals by these tag values to form initial segments.
    *   **Secondary Method (Opportunity Name Parsing):**
        1.  If direct tags are insufficient, absent, or too generic for meaningful segmentation, OR to refine/corroborate tag-based segments, **THEN parse the `opportunities[*].Name` field** for relevant keywords and themes.
        2.  Look for keywords related to specific technologies, business processes, or outcomes that align with **{context_company_name}'s known capabilities** (refer to `NESIC_CAPABILITIES_CONTEXT`). Examples: "Migration", "Cloud", "Security", "Network", "DX", "Consulting", "Managed Service", "Integration", "Analytics", "IoT", specific vendor names (AWS, Azure, Cisco etc. – be cautious not to misinterpret these as NESIC selling competitor products unless the context is clear).
    *   **Application Scope:** Apply this segmentation primarily to the 'Won Deal' subset for quantitative analysis (if available and deals have valid `Amount > 0`), otherwise apply to all opportunities for qualitative analysis.
    *   **Acknowledge Inference & Confidence:** Clearly state the basis of segmentation (e.g., "Based on `CT_Approach_Type__c` field and supplemented by Opportunity Name parsing..."). If confidence in categorization for a significant portion of deals is low due to vague names or tags, state this limitation.
    *   **Handling Ambiguity & Grouping:** If a deal has multiple relevant tags or keywords, assign it to the most dominant/specific theme or use a multi-label approach if appropriate for the analysis. Create logical, slightly broader groupings if necessary (e.g., "Network Infrastructure & Security"). Avoid overly granular or uncertain categorization.
    *   **Account Context (Section 2.1 and 4):** Use Account-level tags (`accounts[0].CT_f_...`, `sci_ttag_...`) mainly for broader client profile context in Section 2.1 and the White Space analysis (Section 4). These reflect the *account's* general profile/interests.
    *   **Focus (Won Deals):** Concentrate on the top 3-5 most significant inferred/tagged categories by revenue and/or deal count for won deals. Calculate metrics like total revenue, deal count, and *average deal size per category* if data permits robust calculation (excluding deals with Amount <= 0 from average calculations).
    *   **Focus (No Won Deals / Qualitative):** Concentrate on the 3-5 most frequently occurring inferred categories or themes across *all* opportunities to understand engagement focus.
    """)
# Assume WHITESPACE_ANALYSIS_INSTRUCTION is defined globally here as previously updated...
WHITESPACE_ANALYSIS_INSTRUCTION = textwrap.dedent("""\
    **White Space Analysis Guidance (Section 4):**

    *   **Objective:** Identify potential untapped service areas or strategic themes for {context_company_name} by comparing the client's profile/needs (from Account-level data) against {context_company_name}'s historical **won** business footprint (from Opportunity-level data, or overall opportunity focus if no won deals).
    *   **Step 1: Profile Context (Account-Level Data):**
        *   Summarize relevant client interests, characteristics, stated needs, or competitor/other services used based on **Account-level** fields.
        *   **CRITICAL:** Parse multi-value string fields like `accounts[0].CT_f_scenarios__c`, `sci_ttag_trends__c`, `sci_ttag_businessAndServices__c`, `sci_ttag_adoptedItServiceCategory__c`, `sci_ttag_services__c`, `CT_f_service_categories__c`, `CT_f_services__c`. Split these comma/semicolon-separated strings into distinct items/tags.
        *   List key themes/items from these parsed tags (e.g., "Client interested in: 'AI', 'Cloud Migration'. Uses: 'Competitor X for CRM'. Trends: 'Remote Work Solutions'.").
    *   **Step 2: Compare with {context_company_name}'s Engagement (Opportunity-Level Data):**
        *   Cross-reference these Account-level profile indicators against the actual Service/Product and DX/Strategic segments where {context_company_name} has achieved **Won Deals** (from Section 2) or themes frequently seen across *all* deals if no/few won deals exist.
    *   **Step 3: Identify & Map Gaps to {context_company_name} Capabilities:**
        *   Explicitly list 2-4 potential service areas or themes suggested by the Account Profile/Tags where {context_company_name} shows **few or no corresponding Won Deals** (or limited engagement overall) in the JSON data.
        *   **CRITICAL: For each identified white space, directly map it to specific {context_company_name} capabilities or service offerings** from the `NESIC_CAPABILITIES_CONTEXT`.
        *   **Prioritize:** Briefly suggest which white space opportunities might be higher priority based on factors like: strong alignment with Account tags (client interest), potential deal size (inferred, if possible), strategic fit with {context_company_name}'s strengths, or perceived ease of entry.
    *   **Frame as Opportunities:** Present these gaps clearly as potential growth opportunities for {context_company_name}.
        *   Example: "- **Opportunity (High Priority):** Account profile tags indicate strong interest in 'Cloud Security (`sci_ttag_adoptedItServiceCategory__c` on Account)' and 'Compliance (`CT_f_scenarios__c` on Account)', but few related Won deals are observed. **Map to {context_company_name}:** Leverage {context_company_name}'s 'Comprehensive Cybersecurity Services' & 'Strategic Cloud Services', emphasizing multi-cloud security and compliance expertise."
    """)
# Assume COMPLETION_CHECKS_JSON is defined globally here as previously provided...
COMPLETION_CHECKS_JSON = textwrap.dedent("""\
    **Completion & Final Review Checklist (Internal AI Check):**

    *   **Completeness:** Are all sections (0-7) present and addressed per instructions?
    *   **Data Source:** Is the analysis strictly based *only* on the provided JSON data?
    *   **Filtering Logic:** Was the `IsWon == true` filter correctly applied for quantitative analysis (and `Amount > 0` for revenue averages)? Was the "No Won Deals" scenario handled appropriately if triggered?
    *   **Error Handling:** Was the initial JSON validation check performed? Was the correct error message outputted if validation failed?
    *   **Segmentation:** Are segments based *first* on structured Opportunity tags (if available/relevant), then supplemented by Name parsing? Is inference clearly noted?
    *   **White Space Analysis:** Does Section 4 effectively compare Account-level profile tags (parsed as lists) against deal history to identify potential gaps/opportunities for {context_company_name}? Are gaps mapped to {context_company_name} capabilities?
    *   **{context_company_name} Perspective:** Is the analysis consistently framed from {context_company_name}'s viewpoint?
    *   **Formatting & Language:** Does the output strictly adhere to Markdown formatting and the target **{language}**? Are units used consistently? Are forbidden placeholders absent?
    *   **Actionability:** Are recommendations in Section 5 specific, justified by data, and strategically relevant for {context_company_name}?
    *   **No Conversational Text:** Is there absolutely no introductory or concluding text outside the defined report structure?
    """)

# Assume get_language_instruction is defined globally here as previously provided...
def get_language_instruction(language: str) -> str:
    """Returns the basic language instruction string."""
    return f"Output Language: The final analysis report **MUST** be presented entirely in **{language}**."


# --- Main Prompt Function ---
def get_analysis_prompt(company_name: str, language: str = "English", context_company_name: str = "NESIC") -> str:
    persona = f"You are an expert Senior Account Strategist and Data Analyst at **{context_company_name}**. Your objective is to meticulously analyze historical transaction data (provided as JSON in a `.txt` file) for the client **{company_name}** and generate a highly insightful, actionable strategic report **solely for internal {context_company_name} use**."

    terms = lang_terms.get(language, lang_terms["English"])
    formatted_terms = {}
    for key, value in terms.items():
        try:
            # Attempt to format with all placeholders, will work if all are present
            formatted_terms[key] = value.format(company_name=company_name, context_company_name=context_company_name, terms=terms) # Added terms for recursive use
        except KeyError:
            # Fallback for partial replacements if some placeholders are missing in a specific term string
            temp_value = value.replace("{company_name}", company_name)
            temp_value = temp_value.replace("{context_company_name}", context_company_name)
            # Add other specific replacements if needed, or a general loop
            formatted_terms[key] = temp_value
        except Exception as e:
            # print(f"Warning: Could not format term '{key}': {e}") # Optional: for debugging
            formatted_terms[key] = value # Fallback to original if complex formatting fails
    terms = formatted_terms

    # Re-format instruction blocks using the fully populated 'terms'
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS_JSON.format(language=language, terms=terms, context_company_name=context_company_name)
    formatted_missing_info = HANDLING_MISSING_INFO_INSTRUCTION_JSON.format(company_name=company_name, terms=terms)
    formatted_json_processing = JSON_DATA_PROCESSING_INSTRUCTIONS.format(company_name=company_name, terms=terms, context_company_name=context_company_name)
    formatted_won_deal_logic = WON_DEAL_FILTERING_LOGIC.format(company_name=company_name, terms=terms)
    formatted_nesic_perspective = NESIC_PERSPECTIVE_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_segmentation = SEGMENTATION_INSTRUCTION.format(terms=terms, context_company_name=context_company_name)
    formatted_whitespace = WHITESPACE_ANALYSIS_INSTRUCTION.format(context_company_name=context_company_name, terms=terms)
    base_formatted_completion_checks = COMPLETION_CHECKS_JSON.format(language=language, terms=terms, context_company_name=context_company_name)

    prompt = f"""
{persona}

**CRITICAL FOCUS:** Generate a strategic analysis report **FOR {context_company_name}** concerning the client **{company_name}**, based **ENTIRELY** on the structured JSON data provided within the `.txt` file.

**Objective:** Produce a detailed, data-driven report identifying historical transaction trends, key business segments involved in **WON deals**, deal characteristics, untapped potential ("White Space"), and actionable strategic recommendations **for {context_company_name}**.

**Input:**
1.  A `.txt` file (e.g., `{company_name}.txt`) containing structured JSON data (`accounts` and `opportunities` lists).
2.  Client Name: `{company_name}` (Ensure this name EXACTLY matches the `Name` or `CT_NameAbbreviation__c` in the account record within the JSON, after trimming whitespace.)
3.  Output Language: `{language}`

**Target Audience:** Internal {context_company_name} Sales & Strategy Teams.

{get_language_instruction(language)}

--- {context_company_name} Capabilities Context (Reference for Mapping Opportunities) ---
{NESIC_CAPABILITIES_CONTEXT}
--- End {context_company_name} Capabilities Context ---

--- Core Instructions & Constraints (MANDATORY ADHERENCE) ---

*   **Data Source (ABSOLUTE):** Base **ALL** analysis **STRICTLY AND SOLELY** on the provided JSON data. No external web search.
*   **Language & Format:** Output **MUST be in {language}** using valid **Markdown** per the structure below. Use tables effectively.
*   **JSON Adherence:** Utilize specified JSON paths. Acknowledge inference where necessary (e.g., segment parsing).

{formatted_json_processing}
{formatted_won_deal_logic}
{formatted_nesic_perspective}
{formatted_segmentation}
{formatted_whitespace}
{formatted_missing_info}
{formatted_base_formatting}

---
## REQUIRED OUTPUT STRUCTURE ({language}):

# {terms['report_title']}

## {terms['exec_summary']}
*   Analyzed Account: {company_name}
*   Analysis Period: [Derive from earliest `CreatedDate` to latest `CloseDate` of relevant opportunities, e.g., YYYY-MM-DD to YYYY-MM-DD. If only fiscal years available, state e.g., FYYYYY - FYZZZZ]
*   {terms['data_quality_limitations']}: [Briefly note if significant data gaps were encountered, e.g., "Limited segmentation detail due to many generic opportunity names" or "Many 'Won' deals lack Amount data, impacting revenue metrics." If no major issues, state "Data generally sufficient for analysis."]
*   Overall Won Business: [Total Won Revenue from valid `Amount > 0` deals] {terms['unit_currency']} across [Total Won Deal Count] {terms['unit_deals']} (or state `{terms['no_won_deals_found']}`).
*   Key Trends (Won Deals): [1-2 sentences on revenue/deal trends - mention acceleration/deceleration if noticeable from annual data. If applicable, or state "Trend analysis not possible due to insufficient data/won deals."].
*   Dominant Won Segments: [1-2 sentences on top 1-2 segments (from Section 2, prioritizing structured tags then Opportunity Name inference) by revenue/volume based on Won deals. Note confidence if inference is weak. If applicable, or state "Segment analysis not possible due to insufficient data/won deals."].
*   Top 1-2 Strategic Opportunities for {context_company_name}: [Identify the most promising areas for future {context_company_name} engagement, explicitly linking White Space (Sec 4) or underserved segments (Sec 2) to specific {context_company_name} service lines].
*   Key Challenges/Considerations for {context_company_name}: [Mention 1-2 primary challenges based on data patterns (e.g., small avg deal size, long lead times, concentration risk) or identified risks (Sec 7)].

## {terms['trend_analysis']}
*   [IF Won Deals with valid `Amount` and `CloseDate` Exist: Present Markdown table: `{terms['year']}` | `{terms['annual_revenue']}` ({terms['unit_currency']}) | `{terms['annual_deal_count']}` ({terms['unit_deals']}) | `{terms['avg_deal_size']}` ({terms['unit_currency']}). Ensure units/labels are clear. Calculate Avg Deal Size only from deals with Amount > 0.]
*   [IF Won Deals Exist: Analyze trends (YoY growth/decline, peaks, acceleration/deceleration). Compare trends between revenue and deal count. Any apparent seasonality if quarterly data allows?]
*   [IF No Won Deals or insufficient data for trends Exist: State: `{terms['no_won_deals_found']}` or "Trend analysis not performed due to insufficient historical won deal data."]

## {terms['segment_analysis']}
*   [State analysis basis: "Based on 'Won' deals (`IsWon == true` with valid `Amount > 0` for revenue metrics) using available structured Opportunity fields (e.g., `CT_Approach_Type__c`, `RecordTypeName__c`, `sci_ttag_...` fields) supplemented by Opportunity Name parsing where necessary." If no/few won deals, state the alternative qualitative basis clearly based on *all* opportunities.]
*   [Optional: Briefly mention: "Qualitative review of *all* opportunity names and tags suggests broader engagement attempts focused on themes like [mention 1-2 frequent themes from non-won deals, if insightful and distinct from won deal themes]."]

### {terms['sbu_division']}
    *   [State: "Deal-level SBU/Division data is not explicit in the provided Opportunity JSON. Account-level context indicates:"]
    *   - Industry: [`accounts[0].CT_IndustryName__c` or "Not specified in Account data"]
    *   - Market Segment: [`accounts[0].CT_MarketSegmentName__c` or "Not specified in Account data"]
    *   - Key Account Tags/Scenarios (parsed from comma/semicolon-separated strings):
        *   `CT_f_scenarios__c`: [List up to 5 distinct items, or "Not specified"]
        *   `sci_ttag_trends__c`: [List up to 5 distinct items, or "Not specified"]
        *   `sci_ttag_businessAndServices__c`: [List up to 5 distinct items, or "Not specified"]

### {terms['service_product']}
    *   [State: "Service/Product segmentation for **Won Deals** (acknowledging inference; mention confidence level if low):"]
    *   [Table/List (Top 3-5 categories by revenue/count for Won Deals): Inferred/Tagged Category | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}) | Avg Deal Size ({terms['unit_currency']}) per Category (Calculate only from deals with Amount > 0). If using `CT_Approach_Type__c` or similar, use those category names.]
    *   [Analysis: Identify key revenue/volume drivers. Compare performance. How do these align with {context_company_name} strengths (from `NESIC_CAPABILITIES_CONTEXT`)?]
    *   [If no/few won deals with valid amounts: Qualitative list of inferred/tagged categories seen across *all* opportunities and their frequency/thematic importance.]

### {terms['dx_strategic']}
    *   [State: "DX/Strategic Area segmentation for **Won Deals** (acknowledging inference from Opportunity Names or relevant tags; mention confidence if low):"]
    *   [Table/List (Top 3-5 themes for Won Deals): Inferred Theme/Area | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}) | Avg Deal Size ({terms['unit_currency']}) per Theme (Calculate only from deals with Amount > 0).]
    *   [Analysis: Which strategic themes (e.g., Cloud, Security, DX Consulting – mapped to `NESIC_CAPABILITIES_CONTEXT`) has {context_company_name} successfully addressed? Are there DX themes in Account tags not reflected in wins?]
    *   [If no/few won deals with valid amounts: Qualitative list of inferred themes across *all* opportunities and their frequency/thematic importance.]

## {terms['deal_characteristics']}
*   {terms['avg_lead_time']} (Won Deals): [Calculated average (`CloseDate` - `CreatedDate`), OR state reason if not calculable (e.g., `{terms['no_won_deals_found']}` / insufficient valid dates for Won deals)] {terms['unit_days']}
*   {terms['deal_size_distribution']} (Won Deals with Amount > 0): [e.g., "X% of Won deals are < Y {terms['unit_currency']}; Y% between Y-Z {terms['unit_currency']}; Z% > Z {terms['unit_currency']}. Mean: A {terms['unit_currency']}, Median: B {terms['unit_currency']}." OR state `{terms['no_won_deals_found']}` or "Not calculable due to insufficient data."]
*   (Optional) Lead Time Variation: [If data allows, comment if lead time varies by inferred deal type/size from Sec 2 (Won Deals).]
*   (Optional) Deal Velocity: [Comment on Won deals closed per year/quarter from Sec 1.]

## {terms['whitespace_analysis']}
### {terms['client_profile_context']}
    *   Account-Level Indicators (Parsed from comma/semicolon-separated string fields in `accounts[0]`):
        *   `CT_f_scenarios__c`: [List key distinct items, or "Not specified"]
        *   `sci_ttag_trends__c`: [List key distinct items, or "Not specified"]
        *   `sci_ttag_businessAndServices__c`: [List key distinct items, or "Not specified"]
        *   `sci_ttag_adoptedItServiceCategory__c`: [List key distinct items, or "Not specified"]
        *   `sci_ttag_services__c` (Other/Competitor Tech Used): [List key distinct items, or "Not specified"]
        *   `CT_f_service_categories__c`: [List key distinct items, or "Not specified"]
        *   `CT_f_services__c`: [List key distinct items, or "Not specified"]
### {terms['comparison_won_deals']}
    *   [Summarize dominant categories/themes where {context_company_name} *has* won business (from Section 2 Won Deal analysis).]
### {terms['identified_whitespace']}
    *   [Explicitly list 2-4 potential service areas/themes derived from Account Profile tags where {context_company_name} shows **few or no corresponding Won Deals**. **Map directly to specific {context_company_name} capabilities/services** (from `NESIC_CAPABILITIES_CONTEXT`) and indicate potential priority.]
    *   Example: - **Opportunity (High Priority):** Account profile shows strong interest in 'Cloud Security (`sci_ttag_adoptedItServiceCategory__c` on Account)' but few related Won deals. **Map to {context_company_name}:** Leverage {context_company_name}'s 'Comprehensive Cybersecurity Services' & 'Strategic Cloud Services', emphasizing multi-cloud security expertise.

## {terms['strategic_recommendations']}
*   **{terms['strengths_leverage']}:** [Based on Sec 2, identify 1-2 high-performing Won areas. Recommend specific actions: e.g., "Leverage success in [Won Area X from Sec 2.2/2.3] by proactively proposing adjacent [{context_company_name} Service Y from Capabilities Context] to existing contacts."]
*   **{terms['focus_development']}:** [Based on Sec 4 White Space and Sec 2 Gaps, identify 1-2 key areas for *new* business. Recommend specific actions: e.g., "Develop targeted campaign for [White Space Area A from Sec 4.3], showcasing {context_company_name}'s [Specific Capability B from Capabilities Context] aligned with client interest tags like `CT_f_scenarios__c` item '[Scenario Z]'."]
*   **{terms['quick_wins']}:** [Suggest immediate actions: e.g., "Revisit lost deals (e.g., where `StageName` is '失注' and `CT_LostReason__c` is '価格') in categories similar to recent large wins in [Category Z] with a refined value proposition or pricing strategy."]
*   **{terms['efficiency_process']}:** [Link characteristics (Sec 3) to actions: e.g., "If avg lead time is long for [Deal Type W], review {context_company_name}'s qualification and proposal process for such deals."]
*   **{terms['overall_posture']}:** [Recommend {context_company_name}'s 3-year strategic goal for this client, justified by the data synthesis.]
*   [Label general market knowledge insights: `({terms['based_on_general_knowledge']})`.]

## {terms['visualization_suggestions']}
*   [Suggest 2-4 specific, relevant chart types.]
    *   Example: - Time-series line chart for Annual Won Revenue & Count (Sec 1).
    *   Example: - Pie/Bar chart for Won Revenue by inferred/tagged Service Category (Sec 2.2).
    *   Example: - Scatter plot of Won Deal Size vs. Lead Time (Sec 3), if data permits.

## {terms['risks_mitigation']}
*   [Identify 2-3 key risks **for {context_company_name}** based *specifically* on the JSON analysis (e.g., high revenue concentration, declining trend, competitor tags in `accounts[0].sci_ttag_services__c`) and propose brief mitigation ideas mapped to {context_company_name} actions/capabilities.]
    *   Example: **Risk:** Account uses '[Competitor Service Z]' (from `accounts[0].sci_ttag_services__c`). **Mitigation:** Proactively showcase {context_company_name}'s differentiated offering in '[{context_company_name} Capability A]' as a superior alternative.

## Final Struct Instructions:
Output the analysis report directly in **{language}** using **Markdown**. Do not include these instructions or conversational text. Ensure all sections (0-7) are generated according to the logic, handling the "No Won Deals" scenario and null/invalid data points correctly. Adhere strictly to formatting and constraints.
---
{{enhanced_completion_checks}}
"""

    enhanced_completion_checks_text = base_formatted_completion_checks + textwrap.dedent("""\
    *   **Richness Checks:** Does the analysis go beyond simple reporting (e.g., commenting on trends, comparing segments, analyzing distributions)? Are recommendations explicitly linked to data findings? Is white space mapped to specific {context_company_name} services? Is the context of *all* deals considered qualitatively where appropriate?
    *   **Data Handling:** Was null/invalid data within records handled gracefully according to instructions (ignored for specific calcs, not breaking aggregations)? Are Amount=0 deals handled correctly in averages?
    *   **Inference Clarity:** Is the basis of segmentation (structured tags vs. name parsing) clearly stated, along with any confidence limitations?
    *   **Tag Parsing:** Are comma/semicolon-separated string fields (both Account and Opportunity level) being treated as lists of individual items for analysis where instructed (e.g., in White Space, SBU/Division context)?
    """)
    prompt = prompt.replace("{{enhanced_completion_checks}}", enhanced_completion_checks_text)
    prompt = prompt.replace("{{ company_name }}", company_name) # Final replacement for any missed spots
    prompt = prompt.replace("{{ context_company_name }}", context_company_name)


    return prompt

# --- Example Usage (Commented Out) ---
# company_name_example = "Example Client Corp"
# context_company_name_example = "NESIC"
#
# # Generate prompt in Japanese
# prompt_jp = get_analysis_prompt(
#     company_name=company_name_example,
#     language="Japanese",
#     context_company_name=context_company_name_example
# )
# print("--- Japanese Prompt ---")
# print(prompt_jp)
# print("\\n--- End Japanese Prompt ---\\n")
#
# # Generate prompt in English
# prompt_en = get_analysis_prompt(
#     company_name=company_name_example,
#     language="English",
#     context_company_name=context_company_name_example
# )
# print("--- English Prompt ---")
# print(prompt_en)
# print("\\n--- End English Prompt ---\\n")