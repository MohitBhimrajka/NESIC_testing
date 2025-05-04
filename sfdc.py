import textwrap
from typing import Optional

# --- Language Definitions ---
# (Keep this updated with accurate translations and terms)
# Assume lang_terms dictionary is defined globally here as previously provided...
lang_terms = {
    "Japanese": {
        "error_not_found": "提供されたJSONファイルに該当する企業「{company_name}」の有効なデータ（アカウント情報または関連する取引情報）が見つかりません。JSONファイルの内容を確認するか、正確な企業名を指定してください。",
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
        "service_product": "2.2 サービス・商材区分（受注案件名・タグ情報からの推測）",
        "dx_strategic": "2.3 DX・戦略領域（受注案件名・タグ情報からの推測）",
        "deal_characteristics": "3. 受注案件 特性分析",
        "avg_lead_time": "平均リードタイム（受注案件：クローズ日 - 作成日）",
        "deal_size_distribution": "受注案件規模 分布",
        "whitespace_analysis": "4. ホワイトスペース分析 / 未開拓ポテンシャル（{context_company_name}視点）",
        "client_profile_context": "クライアントプロファイル・関心領域（アカウント情報）",
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
        "based_on_general_knowledge": "(※市場の一般的知識に基づく考察)",
        "unit_deals": "件",
        "unit_currency": "円", # Assuming JPY
        "unit_days": "日",
        "year": "年度"
    },
    "English": {
        "error_not_found": "Cannot find valid data (Account Information or related Opportunities) for the specified company '{company_name}' in the provided JSON file. Please check the JSON content or provide the correct company name.",
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
        "service_product": "2.2 Service/Product Categories (Inferred from Won Deal Names/Tags)",
        "dx_strategic": "2.3 DX/Strategic Areas (Inferred from Won Deal Names/Tags)",
        "deal_characteristics": "3. Won Deal Characteristics Analysis",
        "avg_lead_time": "Average Lead Time (Won Deals: Close Date - Create Date)",
        "deal_size_distribution": "Won Deal Size Distribution",
        "whitespace_analysis": "4. White Space Analysis / Untapped Potential (from {context_company_name}'s Perspective)",
        "client_profile_context": "Client Profile & Interest Areas (Account Info)",
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
        "based_on_general_knowledge": "(Note: Observation based on general market knowledge)",
        "unit_deals": "deals",
        "unit_currency": "JPY", # Assuming JPY
        "unit_days": "days",
        "year": "FY"
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
    *   **"No Won Deals" Scenario:** If no opportunities linked to `{company_name}` have `IsWon == true`, follow the specific instructions outlined in the `WON_DEAL_FILTERING_LOGIC` section (state the finding, omit quantitative analysis dependent on 'Won' deals, proceed with qualitative analysis based on *all* opportunities and account info).
    *   **Missing Categories within Segments:** If, *after* filtering for `IsWon == true` (where applicable), data for a specific *parsed* category (e.g., a Service/Product inferred from Opportunity Name) results in zero revenue or zero deals, **silently omit only that specific category's line item or bullet point** from the relevant list in Section 2. Do *not* state 'N/A' or 'Zero'.
    *   **Handling Null/Missing/Invalid Fields within Records:**
        *   **`Amount`:** If `Amount` is null, non-numeric, or missing for a specific opportunity record, treat it as `0` for aggregation purposes (e.g., total revenue calculation) *after* applying relevant filters (like `IsWon == true`). However, exclude this record from average deal size calculations if its `Amount` is invalid.
        *   **`CloseDate`, `CreatedDate`:** If either `CloseDate` or `CreatedDate` is null, invalid, or missing for a specific opportunity, that record **MUST be excluded** from any lead time calculation (Section 3). It can still be used for other analyses like name parsing or revenue aggregation if `Amount` is valid.
        *   **Fiscal Period Derivation:** If explicit `FiscalYear`/`FiscalQuarter` fields are unreliable or missing, attempt derivation from `CloseDate`. If `CloseDate` is also invalid, that record cannot be assigned to a fiscal period for trend analysis (Section 1).
        *   **Other Fields:** If fields used for qualitative parsing (like `Name` or tags) are missing or null, that record cannot contribute to that specific qualitative analysis but might still be valid for quantitative metrics if `Amount`, dates, etc., are present.
    *   **Do NOT Omit Sections:** Do *not* omit entire section headings (e.g., `### 2.2 ...`) if *other* categories or data points within that section *are* valid and derivable from the JSON source.
    *   **No Placeholders:** Absolutely **do NOT** state '該当なし', 'N/A', '不明', 'Not Found', 'Data unavailable', or use placeholders like 'XXX {terms['unit_currency']}'. Only present information verifiable and calculable from the valid portions of the JSON data. If a required calculation (like Avg Lead Time) cannot be performed due to lack of 'Won' deals *or* lack of valid date fields in those deals, state the reason clearly but briefly (e.g., "{terms['no_won_deals_found']}" or "Insufficient valid date data for lead time calculation on Won deals.").
    """)
# Assume JSON_DATA_PROCESSING_INSTRUCTIONS is defined globally here as previously updated...
JSON_DATA_PROCESSING_INSTRUCTIONS = textwrap.dedent("""\
    **JSON Data Processing & Field Mapping (MANDATORY):**

    *   **Input:** A single `.txt` file containing JSON with `accounts` (list) and `opportunities` (list) keys. Validate this basic structure first. If invalid, trigger `{terms['error_json_format']}`.
    *   **Account Identification:**
        1. Locate the account object within the `accounts` list where `Name` or `CT_NameAbbreviation__c` strictly matches **`{company_name}`**. Assume the relevant object is `accounts[0]` if only one account is present matching the context. Use case-insensitive comparison if appropriate for robustness.
        2. Extract the `Id` from this matching account object.
        3. If no matching account object is found, trigger the `{terms['error_not_found']}` error.
    *   **Opportunity Filtering:**
        1. Filter the `opportunities` list to retain only objects where `AccountId` matches the Account `Id` identified above.
        2. If this results in an empty list (no opportunities linked to the account), trigger the `{terms['error_not_found']}` error.
    *   **Field Mapping (Use these paths/methods; handle potential nulls/errors gracefully per `HANDLING_MISSING_INFO_INSTRUCTION_JSON`):**
        *   **Client Info (Account Level - Primarily for Context):** `accounts[0].Name`, `accounts[0].Id`, `accounts[0].CT_IndustryName__c` (Industry), `accounts[0].CT_MarketSegmentName__c` (Market Segment), `accounts[0].sci_ttag_trends__c` (Trends Tags), `accounts[0].sci_ttag_businessAndServices__c` (Business Tags), `accounts[0].sci_ttag_services__c` (Competitor/Other Services Tags), `accounts[0].CT_f_scenarios__c` (Client Scenarios/Needs Tags). *Note: These tags might be lists or strings; parse accordingly.*
        *   **Opportunity Info (Deal Level):**
            *   `Opportunity ID`: `opportunities[*].CT_ItemNumber__c` or `opportunities[*].Id` or `CT_SFId__c`. Use the most reliable unique identifier available.
            *   `Revenue/Amount`: `opportunities[*].Amount`. Interpret as {terms['unit_currency']}. **Handle potential null/non-numeric values (treat as 0 for aggregation if filter applies, exclude from averages).**
            *   `Is Won`: `opportunities[*].IsWon` (boolean `true`/`false`). **CRITICAL filter.**
            *   `Fiscal Period`: Use `opportunities[*].FiscalYear` and `opportunities[*].FiscalQuarter` if present and consistently populated. If not, **derive from `opportunities[*].CloseDate`**. Define fiscal year logic (e.g., ending March 31st). Handle invalid/missing `CloseDate` appropriately.
            *   `Created Date`: `opportunities[*].CreatedDate`. Must be a valid date format.
            *   `Close Date`: `opportunities[*].CloseDate`. Must be a valid date format.
            *   `Opportunity Name`: `opportunities[*].Name` (**Primary source for inferring Service/Product/DX Area**). Treat null/empty names carefully.
            *   `Stage Name`: `opportunities[*].StageName` (Can provide context on deal progression/loss reasons if available).
            *   `Approach Type`: `opportunities[*].CT_Approach_Type__c` (Optional context).
            *   `Record Type`: `opportunities[*].RecordTypeName__c` (Optional context).
            *   `Opportunity Tags`: `opportunities[*].sci_ttag_...` (Use cautiously to *supplement* Name parsing).
    """)
# Assume WON_DEAL_FILTERING_LOGIC is defined globally here as previously updated...
WON_DEAL_FILTERING_LOGIC = textwrap.dedent("""\
    **"Won Deal" Filtering Logic & Contextualization (Mandatory):**

    1.  **Create "Won Deal" Subset:** From the filtered opportunities relevant to `{company_name}`, create a specific subset containing only those where `IsWon == true`.
    2.  **Quantitative Analysis Basis:** ALL quantitative analyses (Total/Annual Revenue, Deal Counts, Averages, Lead Time in Sections 1, 2.2, 2.3, 3) **MUST** be performed exclusively on this 'Won Deal' subset, considering only records with valid data for the specific calculation (per `HANDLING_MISSING_INFO_INSTRUCTION_JSON`). Explicitly state this basis (e.g., "Analysis based on deals where IsWon = true").
    3.  **"No Won Deals" Scenario:** If the 'Won Deal' subset is empty:
        *   **State Clearly:** Report `{terms['no_won_deals_found']}` prominently in the Executive Summary (Section 0) and Trend Analysis (Section 1).
        *   **Omit Quantitative Metrics:** Do NOT calculate or display Total/Annual Revenue, Deal Counts, Average Deal Size, or Average Lead Time based on 'Won' deals. Remove or comment out these specific metrics/tables in Sections 0, 1, 3. State clearly why they are omitted (lack of 'Won' deals).
        *   **Adapt Qualitative Analysis:** Sections 2 (Segments), 4 (White Space), and 5 (Recommendations) MUST shift to a qualitative focus. Analyze patterns based on parsing names/tags/other fields from *all* opportunity types (won, lost, open) linked to the account, combined with Account-level information. Clearly state this limitation: "Due to the absence of 'Won' deals in the data, the following segment and strategic analysis is qualitative, based on all opportunity types and account profile information."
    4.  **Context from All Deals (Even if Won Deals Exist):**
        *   **Enhance Qualitative Insights:** Even when 'Won' deals exist and form the basis for quantitative analysis, **use the full set of opportunities (won, lost, open)** to provide broader qualitative context. For example:
            *   In Section 2.1 (SBU/Account Context), briefly mention themes appearing frequently across *all* opportunity names/types to understand the full scope of engagement attempts.
            *   In Section 5 (Recommendations), consider patterns in lost deals (if `StageName` suggests reasons) or frequently proposed but unclosed deals when suggesting areas for focus or process improvement.
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

    *   **Primary Method:** Your primary method for categorizing deals into Service/Product or DX/Strategic segments **MUST be parsing the `opportunities[*].Name` field** for relevant keywords and themes. Apply this primarily to the 'Won Deal' subset for quantitative analysis (if available), otherwise apply to all opportunities for qualitative analysis.
    *   **Keyword Guidance:** Look for keywords related to specific technologies, business processes, or outcomes that align with **{context_company_name}'s known capabilities** (refer to `NESIC_CAPABILITIES_CONTEXT`). Examples: "Migration", "Cloud", "Security", "Network", "DX", "Consulting", "Managed Service", "Integration", "Analytics", "IoT", specific vendor names (AWS, Azure, Cisco etc.).
    *   **Supplement Cautiously:** Use Opportunity-level tags (`sci_ttag_...`, `CT_Approach_Type__c`) or `RecordTypeName__c` to *supplement* or *validate* the parsing of names, but prioritize insights from the `Name` field if available and clear. Disregard ambiguous or overly generic tags.
    *   **Acknowledge Inference & Confidence:** Clearly state that these segmentations are *inferred* based on Opportunity Name parsing and available supplementary fields. **If confidence in categorization for a significant portion of deals is low due to vague names, state this limitation.**
    *   **Handling Ambiguity & Grouping:** If Opportunity Names are ambiguous or contain multiple potential categories, assign them to the most dominant or specific theme, or create a logical, slightly broader grouping (e.g., "Network Infrastructure & Security", "Cloud & Infrastructure Services"). Avoid overly granular or uncertain categorization. If highly ambiguous after considering context, exclude from detailed segment breakdown but mention qualitatively if the revenue/volume is significant.
    *   **Account Context:** Use Account-level tags (`accounts[0].sci_ttag...`, `accounts[0].CT_f_...`) mainly for context in Section 2.1 and the White Space analysis (Section 4), noting they reflect the *account's* profile, not necessarily specific *deal* drivers unless corroborated by patterns in Opportunity Names.
    *   **Focus (Won Deals):** Concentrate on the top 3-5 most significant inferred categories by revenue and/or deal count for won deals. Calculate metrics like total revenue, deal count, and *average deal size per inferred category* if data permits robust calculation.
    *   **Focus (No Won Deals / Qualitative):** Concentrate on the 3-5 most frequently occurring inferred categories or themes across *all* opportunities to understand engagement focus.
    """)
# Assume WHITESPACE_ANALYSIS_INSTRUCTION is defined globally here as previously updated...
WHITESPACE_ANALYSIS_INSTRUCTION = textwrap.dedent("""\
    **White Space Analysis Guidance (Section 4):**

    *   **Objective:** Identify potential untapped service areas or strategic themes for {context_company_name} by comparing the client's profile/needs against {context_company_name}'s historical **won** business footprint (or overall opportunity focus if no won deals).
    *   **Step 1: Profile Context:** Summarize relevant client interests, characteristics, stated needs, or competitor services used based on **Account-level** fields (e.g., `accounts[0].CT_f_scenarios__c`, `sci_ttag_trends__c`, `sci_ttag_businessAndServices__c`, `sci_ttag_services__c`, industry, market segment). Extract specific keywords or themes.
    *   **Step 2: Compare:** Cross-reference these profile indicators against the actual Service/Product and DX/Strategic segments where {context_company_name} has achieved **Won Deals** (from Section 2) or themes frequently seen across *all* deals if no won deals exist.
    *   **Step 3: Identify & Map Gaps:** Explicitly list 2-4 potential service areas or themes suggested by the account profile where {context_company_name} shows **few or no corresponding won deals** (or limited engagement overall) in the JSON data.
        *   **CRITICAL: Map each identified white space directly to specific {context_company_name} capabilities or service offerings** from the `NESIC_CAPABILITIES_CONTEXT`.
        *   **Prioritize:** Briefly suggest which white space opportunities might be higher priority based on factors like strong alignment with Account tags (client interest), potential deal size (inferred from related won deals), or strategic fit with {context_company_name}'s strengths.
    *   **Frame as Opportunities:** Present these gaps clearly as potential growth opportunities for {context_company_name}. Example: "- **Opportunity (High Priority):** Account tags indicate interest in 'Supply Chain Optimization' [`accounts[0].sci_ttag_trends__c`], but few/no won deals exist in this area. **Map to NESIC:** Leverage NESIC's 'Applied IoT & Data Analytics' and 'SI' capabilities to propose targeted solutions."
    """)
# Assume COMPLETION_CHECKS_JSON is defined globally here as previously provided...
COMPLETION_CHECKS_JSON = textwrap.dedent("""\
    **Completion & Final Review Checklist (Internal AI Check):**

    *   **Completeness:** Are all sections (0-7) present and addressed per instructions?
    *   **Data Source:** Is the analysis strictly based *only* on the provided JSON data?
    *   **Filtering Logic:** Was the `IsWon == true` filter correctly applied for quantitative analysis? Was the "No Won Deals" scenario handled appropriately if triggered (correct messaging, omission of quantitative metrics, shift to qualitative)?
    *   **Error Handling:** Was the initial JSON validation check performed? Was the correct error message outputted if validation failed?
    *   **Segmentation:** Are inferred segments clearly noted as such, based primarily on Opportunity Name parsing, and handled correctly whether based on 'Won' deals or 'All' deals?
    *   **White Space Analysis:** Does Section 4 effectively compare the account profile against deal history to identify potential gaps/opportunities for {context_company_name}?
    *   **{context_company_name} Perspective:** Is the analysis consistently framed from {context_company_name}'s viewpoint, linking findings to its capabilities and strategic goals?
    *   **Formatting & Language:** Does the output strictly adhere to Markdown formatting and the target **{language}**? Are units (`{terms['unit_currency']}`, `{terms['unit_deals']}`, `{terms['unit_days']}`) used consistently? Are forbidden placeholders absent?
    *   **Actionability:** Are the recommendations in Section 5 specific, justified by the data analysis, and strategically relevant for {context_company_name}?
    *   **No Conversational Text:** Is there absolutely no introductory or concluding text outside the defined report structure?
    """)

# Assume get_language_instruction is defined globally here as previously provided...
def get_language_instruction(language: str) -> str:
    """Returns the basic language instruction string."""
    # Simple function, can be expanded if needed for more language nuances
    return f"Output Language: The final analysis report **MUST** be presented entirely in **{language}**."


# --- Main Prompt Function ---
def get_analysis_prompt(company_name: str, language: str = "English", context_company_name: str = "NESIC") -> str:
#     """
#     Generates the OPTIMIZED analysis prompt for Salesforce JSON data.
#     Focuses on extracting deep, actionable strategic intelligence FOR NESIC,
#     leveraging detailed JSON structure and explicitly identifying untapped potential.
#     """
    # --- Role Assignment ---
    persona = f"You are an expert Senior Account Strategist and Data Analyst at **{context_company_name}**. Your objective is to meticulously analyze historical transaction data (provided as JSON in a `.txt` file) for the client **{company_name}** and generate a highly insightful, actionable strategic report **solely for internal {context_company_name} use**."

    # --- Context Setup ---
    context_str = f"**{company_name}**"
    # (Ticker/Industry could be added if available in JSON account info and needed, but often less critical here)

    # --- Retrieve and Format Language Terms ---
    # Assume lang_terms is defined globally as in the original file
    terms = lang_terms.get(language, lang_terms["English"])
    formatted_terms = {}
    for key, value in terms.items():
        # Basic formatting to handle potential placeholders
        try:
            formatted_terms[key] = value.format(company_name=company_name, context_company_name=context_company_name)
        except KeyError: # Handle cases where only one placeholder might be present
             formatted_terms[key] = value.replace("{company_name}", company_name).replace("{context_company_name}", context_company_name)
        except Exception: # Fallback for any other formatting issues
            formatted_terms[key] = value
    terms = formatted_terms # Use the fully formatted dictionary


    # --- Format Instruction Blocks ---
    # Assume instruction blocks (like BASE_FORMATTING_INSTRUCTIONS_JSON, etc.) are defined globally and updated as per previous response
    # We use the UPDATED versions of these blocks here.
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS_JSON.format(language=language, terms=terms, context_company_name=context_company_name)
    formatted_missing_info = HANDLING_MISSING_INFO_INSTRUCTION_JSON.format(company_name=company_name, terms=terms)
    formatted_json_processing = JSON_DATA_PROCESSING_INSTRUCTIONS.format(company_name=company_name, terms=terms)
    formatted_won_deal_logic = WON_DEAL_FILTERING_LOGIC.format(company_name=company_name, terms=terms)
    formatted_nesic_perspective = NESIC_PERSPECTIVE_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_segmentation = SEGMENTATION_INSTRUCTION.format(terms=terms, context_company_name=context_company_name) # Added context_company_name for keyword guidance
    formatted_whitespace = WHITESPACE_ANALYSIS_INSTRUCTION.format(context_company_name=context_company_name)
    # Base completion checks are defined globally, we'll append to it later
    base_formatted_completion_checks = COMPLETION_CHECKS_JSON.format(language=language, terms=terms, context_company_name=context_company_name)


    # --- Assemble the Final Prompt ---
    prompt = f"""
{persona}

**CRITICAL FOCUS:** Generate a strategic analysis report **FOR {context_company_name}** concerning the client **{company_name}**, based **ENTIRELY** on the structured JSON data provided within the `.txt` file.

**Objective:** Produce a detailed, data-driven report identifying historical transaction trends, key business segments involved in **WON deals**, deal characteristics, untapped potential ("White Space"), and actionable strategic recommendations **for {context_company_name}**.

**Input:**
1.  A `.txt` file (e.g., `{company_name}.txt`) containing structured JSON data (`accounts` and `opportunities` lists).
2.  Client Name: `{company_name}`
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
{formatted_won_deal_logic} # Includes using context from all deals
{formatted_nesic_perspective}
{formatted_segmentation} # Includes keyword guidance
{formatted_whitespace} # Includes mapping to NESIC services & prioritization
{formatted_missing_info} # Includes handling nulls within records
{formatted_base_formatting} # Includes table example emphasis
# (Include any other STANDARD blocks adapted for JSON, e.g., Specificity based on dates)

---
## REQUIRED OUTPUT STRUCTURE ({language}):

# {terms['report_title']}

## {terms['exec_summary']}
*   Analyzed Account: {company_name}
*   Analysis Period: [Range covering relevant opportunities, e.g., FY2021-FY2023 derived from dates/fiscal fields]
*   Overall Won Business: [Total Won Revenue] {terms['unit_currency']} across [Total Won Deal Count] {terms['unit_deals']} (or state `{terms['no_won_deals_found']}`). Handle potential calculation issues due to null Amounts.
*   Key Trends (Won Deals): [1-2 sentences on revenue/deal trends - mention acceleration/deceleration if noticeable. If applicable].
*   Dominant Won Segments: [1-2 sentences on top 1-2 inferred Service/Product or DX areas by revenue/volume based on Won deals. Note confidence if inference is weak. If applicable].
*   Top 1-2 Strategic Opportunities for {context_company_name}: [Identify the most promising areas for future {context_company_name} engagement, explicitly linking White Space (Sec 4) or underserved segments (Sec 2) to specific {context_company_name} service lines].
*   Key Challenges/Considerations for {context_company_name}: [Mention 1-2 primary challenges based on data patterns (e.g., small avg deal size, long lead times, concentration risk) or identified risks (Sec 7)].

## {terms['trend_analysis']}
*   [IF Won Deals Exist: Present Markdown table: `FiscalYear` | `{terms['annual_revenue']}` ({terms['unit_currency']}) | `{terms['annual_deal_count']}` ({terms['unit_deals']}) | `{terms['avg_deal_size']}` ({terms['unit_currency']}). Ensure units/labels are clear. Handle potential calculation issues due to null Amounts.]
*   [IF Won Deals Exist: Analyze trends (YoY growth/decline, peaks, acceleration/deceleration). Compare trends between revenue and deal count. Any apparent seasonality if quarterly data allows?]
*   [IF No Won Deals Exist: State: `{terms['no_won_deals_found']}`]

## {terms['segment_analysis']}
*   [State analysis basis: "Primarily based on Won Deals (`IsWon == true`) unless otherwise noted." If no won deals, state the alternative qualitative basis clearly.]
*   Briefly mention: "Qualitative review of *all* opportunity names suggests broader engagement attempts focused on themes like [mention 1-2 frequent themes from non-won deals, if insightful]."

### {terms['sbu_division']}
    *   [State: "Deal-level SBU data is not explicit in the provided JSON. Account-level context indicates:"]
    *   - Industry: [`accounts[0].CT_IndustryName__c` or "Not specified"]
    *   - Market Segment: [`accounts[0].CT_MarketSegmentName__c` or "Not specified"]
    *   - Key Account Tags/Scenarios: [List 2-3 most relevant from `accounts[0].CT_f_...`, `sci_ttag_...` fields if present]

### {terms['service_product']}
    *   [State: "Based primarily on parsing Opportunity Names & available tags for **Won Deals** (acknowledging inference; mention confidence level if low):"]
    *   [Table/List: Inferred Category | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}) | Avg Deal Size ({terms['unit_currency']}) per Category (Calculate if feasible). Highlight Top 3-5 categories by revenue/count.]
    *   [Analysis: Identify key revenue/volume drivers within Won deals. Compare performance across top categories (e.g., higher volume but lower avg size?). How do these align with {context_company_name} strengths?]
    *   [If no won deals: Qualitative list of inferred categories seen across *all* opportunities and their frequency.]

### {terms['dx_strategic']}
    *   [State: "Based primarily on parsing Opportunity Names & fields for **Won Deals** (acknowledging inference; mention confidence level if low):"]
    *   [Table/List: Inferred Theme/Area | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}) | Avg Deal Size ({terms['unit_currency']}) per Theme (Calculate if feasible). Highlight Top 3-5 themes by revenue/count.]
    *   [Analysis: Which strategic themes has {context_company_name} successfully addressed based on Won deals? Are there related DX themes mentioned in Account tags but not reflected in wins?]
    *   [If no won deals: Qualitative list of inferred themes across *all* opportunities and their frequency.]

## {terms['deal_characteristics']}
*   {terms['avg_lead_time']} (Won Deals): [Calculated average (`CloseDate` - `CreatedDate`), OR state reason if not calculable (no won deals / insufficient valid dates)] {terms['unit_days']}
*   {terms['deal_size_distribution']} (Won Deals): [Provide more detail: e.g., "Approx X% of Won deals are below Y {terms['unit_currency']}, with a few significant deals > Z {terms['unit_currency']}." Use quantiles or bands if derivable. OR state `{terms['no_won_deals_found']}`].
*   (Optional) Lead Time Variation: [Does lead time appear to vary significantly by inferred deal type/size from Sec 2 (Won Deals)? E.g., "Larger SI projects show notably longer lead times."]
*   (Optional) Deal Velocity: [Comment on the number of Won deals closed per year/quarter, if trend data (Sec 1) shows interesting patterns. E.g., "Deal closure rate appears consistent..." or "...accelerated in FYZZZZ."]

## {terms['whitespace_analysis']}
### {terms['client_profile_context']}
    *   [List key relevant tags/scenarios/services used from Account fields, focusing on unmet needs or competitor services. E.g., "Tags indicate interest in: [Trend A], [Need B]. Uses competitor service for: [Service C]."]
### {terms['comparison_won_deals']}
    *   [Summarize dominant categories/themes where {context_company_name} *has* won business (from Section 2).]
### {terms['identified_whitespace']}
    *   [Explicitly list 2-4 potential service areas/themes derived from Account Profile/Tags where {context_company_name} shows **few or no corresponding Won Deals**. **Map directly to specific {context_company_name} capabilities/services** and indicate potential priority.]
    *   Example: - **Opportunity (High Priority):** Account profile shows strong interest in `Cloud Security` [`accounts[0].sci_ttag_...`] but few related Won deals. **Map to NESIC:** Leverage 'Comprehensive Cybersecurity Services' & 'Strategic Cloud Services', emphasizing multi-cloud security expertise.
    *   Example: - **Opportunity (Med Priority):** Account uses competitor for `Basic Network Monitoring` [`accounts[0].sci_ttag_services__c`]. **Map to NESIC:** Potential displacement using 'Intelligent Managed Services' with superior automation/reporting.

## {terms['strategic_recommendations']}
*   **{terms['strengths_leverage']}:** [Based on Sec 2, identify 1-2 high-performing (revenue/volume) Won areas. Recommend specific actions: e.g., "Leverage success in [Won Area X] by proactively proposing adjacent [NESIC Service Y] to existing contacts."]
*   **{terms['focus_development']}:** [Based on Sec 4 White Space and Sec 2 Gaps, identify 1-2 key areas for *new* business. Recommend specific actions: e.g., "Develop targeted campaign for [White Space Area A], showcasing {context_company_name}'s [Specific Capability B] aligned with client interest tags."]
*   **{terms['quick_wins']}:** [Suggest immediate actions based on data: e.g., "Revisit lost deals similar to recent large wins in [Category Z] with updated value proposition"; "Target accounts showing high interest tags but low conversion (if inferrable)."]
*   **{terms['efficiency_process']}:** [Link characteristics (Sec 3) to actions: e.g., "If avg lead time is long for [Deal Type W], review {context_company_name}'s qualification process for such deals"; "If avg deal size is small, explore bundling or tiered service offerings."]
*   **{terms['overall_posture']}:** [Recommend {context_company_name}'s 3-year strategic goal, explicitly justified by the data synthesis: e.g., "Given strong performance in [Area X] but significant white space in [Area Y], recommend a strategy of 'Defend Core & Expand Adjacencies', focusing new business development on [Area Y] leveraging [NESIC Strength Z]."]
*   [Label general knowledge insights: `({terms['based_on_general_knowledge']})`.]

## {terms['visualization_suggestions']}
*   [Suggest 2-4 specific, relevant chart types.]
    *   Example: - Time-series line chart for Annual Won Revenue & Count (Sec 1).
    *   Example: - Stacked Bar or Treemap chart for Won Revenue by inferred Service Category over time (Sec 2.2).
    *   Example: - Scatter plot of Won Deal Size vs. Lead Time (Sec 3), if data permits.
    *   Example: - Heatmap comparing Account Interest Tags vs. Won Deal Categories (visualizing Sec 4).

## {terms['risks_mitigation']}
*   [Identify 2-3 key risks **for {context_company_name}** based *specifically* on the JSON analysis (e.g., high revenue concentration in one inferred service, declining trend in a key segment, long lead times indicating potential process issues, presence of competitor tags on Account) and propose brief mitigation ideas.]
    *   Example: **Risk:** Over-reliance on inferred "[Service X]" (represents Y% of Won revenue). **Mitigation:** Prioritize business development in identified white space areas [Area A, B] (Sec 4) and cross-sell efforts within existing contacts.

## Final Struct Instructions:
Output the analysis report directly in **{language}** using **Markdown**. Do not include these instructions or conversational text. Ensure all sections (0-7) are generated according to the logic, handling the "No Won Deals" scenario and null/invalid data points correctly. Adhere strictly to formatting and constraints.
---
{{enhanced_completion_checks}}
""" # End of main prompt f-string

    # Append the enhanced completion checks dynamically
    enhanced_completion_checks_text = base_formatted_completion_checks + textwrap.dedent("""\
    *   **Richness Checks:** Does the analysis go beyond simple reporting (e.g., commenting on trends, comparing segments, analyzing distributions)? Are recommendations explicitly linked to data findings? Is white space mapped to specific NESIC services? Is the context of *all* deals considered qualitatively?
    *   **Data Handling:** Was null/invalid data within records handled gracefully according to instructions (ignored for specific calcs, not breaking aggregations)?
    *   **Inference Clarity:** Is the inferred nature of segmentation clearly stated, along with any confidence limitations?
    """)
    prompt = prompt.replace("{{enhanced_completion_checks}}", enhanced_completion_checks_text)


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