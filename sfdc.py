import textwrap
from typing import Optional

# --- Language Definitions ---
# (Keep this updated with accurate translations and terms)
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
# (Keep this updated with accurate public/sharable NESIC info)
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

BASE_FORMATTING_INSTRUCTIONS_JSON = textwrap.dedent("""\
    **Output Format & Quality Requirements:**

    *   **Direct Start & No Conversational Text:** Begin the response *directly* with the report title (`# {terms['report_title']}`). Absolutely no introductory or concluding remarks outside the defined structure.
    *   **Strict Markdown Formatting:** Use valid and consistent Markdown throughout. Adhere precisely to the heading levels (`#`, `##`, `###`) specified in the REQUIRED OUTPUT STRUCTURE. Use bullets (`*` or `-`) for lists.
    *   **Tables:** Use perfectly formatted Markdown tables for trends and segment breakdowns where requested. Ensure headers are clear and data alignment is logical (numbers right-aligned if possible).
    *   **Conciseness & Clarity:** Be specific and analytical. Avoid jargon where possible, but use appropriate business terms. Ensure clear topic sentences for paragraphs.
    *   **Data Formatting Consistency:** Use appropriate thousands separators for numbers per the target language: **{language}**. Always specify the currency unit (`{terms['unit_currency']}`) for monetary values. Format periods consistently (e.g., YYYY {terms['year']} QX). Use specified units (`{terms['unit_deals']}`, `{terms['unit_days']}`).
    *   **Tone:** Professional, analytical, objective, and **strategically focused from the perspective of {context_company_name}**.
    """)

HANDLING_MISSING_INFO_INSTRUCTION_JSON = textwrap.dedent("""\
    **Handling Missing or Zero-Value Data in JSON Analysis:**

    *   **Basis:** All analysis MUST stem from the provided JSON data for `{company_name}`.
    *   **"No Won Deals" Scenario:** If no opportunities linked to `{company_name}` have `IsWon == true`, follow the specific instructions outlined in the `WON_DEAL_FILTERING_LOGIC` section (state the finding, omit quantitative analysis, proceed with qualitative analysis based on *all* opportunities and account info).
    *   **Missing Categories within Segments:** If, *after* filtering for `IsWon == true` (where applicable), data for a specific *parsed* category (e.g., a Service/Product inferred from Opportunity Name) results in zero revenue or zero deals, **silently omit only that specific category's line item or bullet point** from the relevant list in Section 2.
    *   **Do NOT Omit Sections:** Do *not* omit entire section headings (e.g., `### 2.2 ...`) if *other* categories within that section *do* have valid data based on the JSON source.
    *   **No Placeholders:** Absolutely **do NOT** state '該当なし', 'N/A', '不明', 'Not Found', 'Data unavailable', or use placeholders like 'XXX {terms['unit_currency']}'. Only present information verifiable from the filtered JSON data. If a required calculation (like Avg Lead Time) cannot be performed due to lack of 'Won' deals, state `{terms['no_won_deals_found']}` as instructed for that specific metric.
    """)

JSON_DATA_PROCESSING_INSTRUCTIONS = textwrap.dedent("""\
    **JSON Data Processing & Field Mapping (MANDATORY):**

    *   **Input:** A single `.txt` file containing JSON with `accounts` (list) and `opportunities` (list) keys. Validate this basic structure first. If invalid, trigger `{terms['error_json_format']}`.
    *   **Account Identification:**
        1. Locate the account object within the `accounts` list where `Name` or `CT_NameAbbreviation__c` strictly matches **`{company_name}`**. Assume the relevant object is `accounts[0]` if only one account is present matching the context.
        2. Extract the `Id` from this matching account object.
        3. If no matching account object is found, trigger the `{terms['error_not_found']}` error.
    *   **Opportunity Filtering:**
        1. Filter the `opportunities` list to retain only objects where `AccountId` matches the Account `Id` identified above.
        2. If this results in an empty list (no opportunities linked to the account), trigger the `{terms['error_not_found']}` error.
    *   **Field Mapping (Use these exact paths/methods):**
        *   **Client Info (Account Level - Primarily for Context):** `accounts[0].Name`, `accounts[0].Id`, `accounts[0].CT_IndustryName__c`, `accounts[0].CT_MarketSegmentName__c`, `accounts[0].sci_ttag_...`, `accounts[0].CT_f_...`
        *   **Opportunity Info (Deal Level):**
            *   `Opportunity ID`: `opportunities[*].CT_ItemNumber__c` or `CT_SFId__c`.
            *   `Revenue/Amount`: `opportunities[*].Amount`. Interpret as {terms['unit_currency']}. Handle potential non-numeric or null values gracefully (treat as 0 for aggregation if filtering applies, otherwise ignore the record for that specific calculation).
            *   `Is Won`: `opportunities[*].IsWon` (boolean `true`/`false`). **This is the CRITICAL filter.**
            *   `Fiscal Period`: Use `opportunities[*].FiscalYear` and `opportunities[*].FiscalQuarter` if present and reliable. If not, derive from `opportunities[*].CloseDate`. Prioritize explicit fiscal fields if available.
            *   `Created Date`: `opportunities[*].CreatedDate`.
            *   `Close Date`: `opportunities[*].CloseDate`.
            *   `Opportunity Name`: `opportunities[*].Name` (**Primary source for inferring Service/Product/DX Area**).
            *   `Approach Type`: `opportunities[*].CT_Approach_Type__c`.
            *   `Record Type`: `opportunities[*].RecordTypeName__c`.
            *   `Opportunity Tags`: `opportunities[*].sci_ttag_...` (Use cautiously to *supplement* Name parsing).
    """)

WON_DEAL_FILTERING_LOGIC = textwrap.dedent("""\
    **"Won Deal" Filtering Logic (Mandatory):**

    1.  **Create Subset:** From the filtered opportunities relevant to `{company_name}`, create a specific subset containing only those where `IsWon == true`.
    2.  **Quantitative Analysis Basis:** ALL quantitative analyses (Total/Annual Revenue, Deal Counts, Averages in Sections 1, 2.2, 2.3, 3) **MUST** be performed exclusively on this 'Won Deal' subset. Explicitly state this basis.
    3.  **"No Won Deals" Scenario:** If the 'Won Deal' subset is empty:
        *   **State Clearly:** Report `{terms['no_won_deals_found']}` prominently in the Executive Summary (Section 0) and Trend Analysis (Section 1).
        *   **Omit Quantitative Metrics:** Do NOT calculate or display Total/Annual Revenue, Deal Counts, Average Deal Size, or Average Lead Time. Remove or comment out these specific metrics/tables in Sections 0, 1, 2, 3.
        *   **Adapt Qualitative Analysis:** Sections 2 (Segments) and 5 (Recommendations) MUST shift to a qualitative focus. Analyze patterns based on parsing names/tags from *all* opportunity types (won, lost, open) linked to the account, combined with Account-level information. Clearly state this limitation: "Due to the absence of 'Won' deals in the data, the following segment and strategic analysis is qualitative, based on all opportunity types and account profile information."
        *   Section 4 (White Space) should still be attempted, comparing Account profile context against the themes found in *all* opportunities.
    """)

NESIC_PERSPECTIVE_INSTRUCTION = textwrap.dedent("""\
    **{context_company_name} Perspective Integration (CRITICAL):**

    *   **Viewpoint:** Frame **ALL** analysis, observations, identified opportunities, risks, and recommendations explicitly from the perspective of **{context_company_name}**. The central question is: "What does this data tell *us* ({context_company_name}) about how to strategically engage and grow our business with {company_name}?"
    *   **Capability Mapping:** Actively connect findings from the JSON data (trends, segments, client needs inferred from deal names/account tags) to specific **{context_company_name}** capabilities, strengths, and differentiators (as listed in the `NESIC_CAPABILITIES_CONTEXT`).
    *   **Value Proposition:** Articulate the potential value {context_company_name} can bring based on the analysis (e.g., "The prevalence of [X type] deals suggests NESIC's strength in [Y capability] is well-received and can be further leveraged.").
    """)

SEGMENTATION_INSTRUCTION = textwrap.dedent("""\
    **Segmentation Analysis Guidance (Sections 2.2 & 2.3):**

    *   **Primary Method:** Your primary method for categorizing deals into Service/Product or DX/Strategic segments **MUST be parsing the `opportunities[*].Name` field** for relevant keywords and themes, applied to the 'Won Deal' subset (if available, otherwise apply to all opportunities for qualitative analysis).
    *   **Supplement Cautiously:** Use Opportunity-level tags (`sci_ttag_...`, `CT_Approach_Type__c`) to *supplement* the parsing of names, but prioritize insights from the name field if available and clear.
    *   **Acknowledge Inference:** Clearly state that these segmentations are *inferred* based on Opportunity Name parsing and available tags, as dedicated segment fields are not present in the provided JSON structure.
    *   **Handling Ambiguity:** If Opportunity Names are ambiguous or contain multiple potential categories, assign them to the most likely category based on common business understanding, or create a logical grouping (e.g., "Network Infrastructure & Security"). Avoid overly granular or uncertain categorization; if highly ambiguous, potentially exclude from detailed segment breakdown but mention qualitatively.
    *   **Account Context:** Use Account-level tags (`accounts[0].sci_ttag...`, `accounts[0].CT_f_...`) mainly for context in Section 2.1 and the White Space analysis (Section 4), noting they reflect the *account's* profile, not necessarily specific *deal* drivers unless corroborated by patterns in Opportunity Names.
    *   **Focus (Won Deals):** Concentrate on the top 3-5 most significant inferred categories by revenue and/or deal count for won deals.
    *   **Focus (No Won Deals):** Concentrate on the 3-5 most frequently occurring inferred categories across *all* opportunities.
    """)

WHITESPACE_ANALYSIS_INSTRUCTION = textwrap.dedent("""\
    **White Space Analysis Guidance (Section 4):**

    *   **Objective:** Identify potential untapped service areas or strategic themes for {context_company_name} based on the client's profile vs. {context_company_name}'s historical **won** business (or overall opportunity focus if no won deals).
    *   **Step 1: Profile Context:** Summarize relevant client interests, characteristics, or stated needs based on **Account-level** fields (`accounts[0].CT_f_scenarios__c`, `sci_ttag_trends__c`, `sci_ttag_businessAndServices__c`, `CT_IndustryName__c`, `CT_MarketSegmentName__c`). Also consider services they use from others (`accounts[0].sci_ttag_services__c`).
    *   **Step 2: Compare:** Cross-reference these profile indicators against the actual Service/Product and DX/Strategic segments identified from **Won Deals** in Section 2 (or themes from *all* deals if no won deals exist).
    *   **Step 3: Identify Gaps:** Explicitly list potential service areas or strategic themes suggested by the account profile where {context_company_name} shows **few or no corresponding won deals** (or limited engagement overall) in the JSON data. These are potential white spaces. Explicitly link the white space to the Account-level indicator or competitor service tag.
    """)

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

# --- Helper Function ---
def get_language_instruction(language: str) -> str:
    """Returns the basic language instruction string."""
    # Simple function, can be expanded if needed for more language nuances
    return f"Output Language: The final analysis report **MUST** be presented entirely in **{language}**."

# --- Main Prompt Function ---
def get_analysis_prompt(company_name: str, language: str = "English", context_company_name: str = "NESIC") -> str:
    """
    Generates the OPTIMIZED analysis prompt for Salesforce JSON data.
    Focuses on extracting deep, actionable strategic intelligence FOR NESIC,
    leveraging detailed JSON structure and explicitly identifying untapped potential.
    """
    # --- Role Assignment ---
    persona = f"You are an expert Senior Account Strategist and Data Analyst at **{context_company_name}**. Your objective is to meticulously analyze historical transaction data (provided as JSON in a `.txt` file) for the client **{company_name}** and generate a highly insightful, actionable strategic report **solely for internal {context_company_name} use**."

    # --- Context Setup ---
    context_str = f"**{company_name}**"
    # (Ticker/Industry could be added if available in JSON account info and needed, but often less critical here)

    # --- Retrieve and Format Language Terms ---
    terms = lang_terms.get(language, lang_terms["English"])
    formatted_terms = {}
    for key, value in terms.items():
        if "{company_name}" in value or "{context_company_name}" in value:
            try:
                formatted_terms[key] = value.format(company_name=company_name, context_company_name=context_company_name)
            except KeyError:
                formatted_terms[key] = value.replace("{company_name}", company_name).replace("{context_company_name}", context_company_name)
        else:
            formatted_terms[key] = value
    terms = formatted_terms # Use the fully formatted dictionary

    # --- Format Instruction Blocks ---
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS_JSON.format(language=language, terms=terms, context_company_name=context_company_name)
    formatted_missing_info = HANDLING_MISSING_INFO_INSTRUCTION_JSON.format(company_name=company_name, terms=terms)
    formatted_json_processing = JSON_DATA_PROCESSING_INSTRUCTIONS.format(company_name=company_name, terms=terms)
    formatted_won_deal_logic = WON_DEAL_FILTERING_LOGIC.format(company_name=company_name, terms=terms)
    formatted_nesic_perspective = NESIC_PERSPECTIVE_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_segmentation = SEGMENTATION_INSTRUCTION.format(terms=terms)
    formatted_whitespace = WHITESPACE_ANALYSIS_INSTRUCTION.format(context_company_name=context_company_name)
    formatted_completion_checks = COMPLETION_CHECKS_JSON.format(language=language, terms=terms, context_company_name=context_company_name)

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
{formatted_won_deal_logic}
{formatted_nesic_perspective}
{formatted_segmentation}
{formatted_whitespace}
{formatted_missing_info}
{formatted_base_formatting}
# (Include any other STANDARD blocks adapted for JSON, e.g., Specificity based on dates)

---
## REQUIRED OUTPUT STRUCTURE ({language}):

# {terms['report_title']}

## {terms['exec_summary']}
*   **Analyzed Account:** {company_name}
*   **Analysis Period:** [Range of `FiscalYear`/`FiscalQuarter` covering all relevant opportunities]
*   **Overall Won Business:** [Total Won Revenue] {terms['unit_currency']} across [Total Won Deal Count] {terms['unit_deals']} (or state `{terms['no_won_deals_found']}`).
*   **Key Trends (Won Deals):** [1-2 sentences on revenue/deal trends, if applicable].
*   **Dominant Won Segments:** [1 sentence on top inferred Service/Product or DX areas based on Won deals, if applicable].
*   **Top 1-2 Opportunities for {context_company_name}:** [Identify the most promising areas for future {context_company_name} engagement based on the full analysis, especially White Space].
*   **Key Challenges/Considerations for {context_company_name}:** [Mention 1-2 primary challenges {context_company_name} faces in growing this account, based on data patterns or risks].

## {terms['trend_analysis']}
*   [IF Won Deals Exist: Present Markdown table: `FiscalYear` | `{terms['annual_revenue']}` | `{terms['annual_deal_count']}` | `{terms['avg_deal_size']}`. Ensure units.]
*   [IF Won Deals Exist: Analyze trends (YoY growth/decline, peaks) observed.]
*   [IF No Won Deals Exist: State: `{terms['no_won_deals_found']}`]

## {terms['segment_analysis']}
*   [State analysis basis: "Based on Won Deals (`IsWon == true`) unless otherwise specified." If no won deals, state the alternative qualitative basis clearly.]

### {terms['sbu_division']}
    *   [State: "Deal-level SBU data is not explicit. Account-level context indicates:"]
    *   - Industry: [`accounts[0].CT_IndustryName__c`]
    *   - Market Segment: [`accounts[0].CT_MarketSegmentName__c`]
    *   (Optional: "- Inferred Areas (All Deal Types): [Qualitative summary based on *all* opportunity names/types, if insightful and no won deals exist.]")

### {terms['service_product']}
    *   [State: "Based primarily on parsing Opportunity Names & tags for **Won Deals** (acknowledging inference):"]
    *   [Table/List: Inferred Category | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}). Highlight Top 3-5.]
    *   [Analysis: Identify revenue/volume drivers within Won deals. Which areas are NESIC's strengths here?]
    *   [If no won deals: Qualitative list of inferred categories seen across *all* opportunities.]

### {terms['dx_strategic']}
    *   [State: "Based primarily on parsing Opportunity Names & fields for **Won Deals** (acknowledging inference):"]
    *   [Table/List: Inferred Theme/Area | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}). Highlight Top 3-5.]
    *   [Analysis: Identify strategic themes NESIC has successfully addressed.]
    *   [If no won deals: Qualitative list of inferred themes across *all* opportunities.]

## {terms['deal_characteristics']}
*   {terms['avg_lead_time']} (Won Deals): [Calculated average (`CloseDate` - `CreatedDate`), OR `{terms['no_won_deals_found']}`] {terms['unit_days']}
*   {terms['deal_size_distribution']} (Won Deals): [Qualitative analysis - e.g., "Predominantly smaller deals (< X JPY) with occasional larger projects.", OR `{terms['no_won_deals_found']}`].
*   (Optional: Lead Time Variation Analysis: [Comment on correlation with inferred type/size for won deals, if data allows]).

## {terms['whitespace_analysis']}
### {terms['client_profile_context']}
    *   [List key relevant tags/scenarios/services used from `accounts[0].CT_f_scenarios__c`, `sci_ttag_trends__c`, `sci_ttag_businessAndServices__c`, `sci_ttag_services__c` etc.]
### {terms['comparison_won_deals']}
    *   [Summarize dominant categories from Section 2 (Won Deals, if applicable).]
### {terms['identified_whitespace']}
    *   [Explicitly list 2-4 potential service areas/themes derived from Account Profile/Tags where {context_company_name} shows **few or no corresponding Won Deals**. Frame as opportunities.]
    *   Example: - **Opportunity:** Client interest in "[Scenario X]" aligns with [{context_company_name} Service Y], yet no won deals reflect this. Potential for proactive proposal.
    *   Example: - **Opportunity:** Client uses competitor "[Service Z]", indicating a potential displacement opportunity for {context_company_name}'s [Service W].

## {terms['strategic_recommendations']}
*   **{terms['strengths_leverage']}:** [Identify 1-2 historically strong (won) inferred areas for NESIC to defend and potentially upsell/cross-sell adjacent solutions.]
*   **{terms['focus_development']}:** [Based on trends, segment gaps, and **Section 4 White Space**, identify 1-2 key areas for NESIC to prioritize for *new* business development/targeted campaigns.]
*   **{terms['quick_wins']}:** [Suggest any immediate actions based on data (e.g., follow-up on recent large wins, re-engage on recurring lost opportunity types with a refined pitch).]
*   **{terms['efficiency_process']}:** [Comment if lead time/deal size/distribution suggests specific sales qualification or process improvements for NESIC with this client.]
*   **{terms['overall_posture']}:** [Recommend NESIC's 3-year strategic goal: e.g., "Maintain current footprint", "Expand into adjacent services (Area X, Y)", "Elevate to strategic DX partner focusing on Area Z". Justify with data.]
*   [Label general knowledge insights: `({terms['based_on_general_knowledge']})`.]

## {terms['visualization_suggestions']}
*   [Suggest 2-3 relevant chart types.]
    *   Example: - Time-series line chart for Annual Won Revenue & Count (Sec 1).
    *   Example: - Bar/Pie chart for Won Revenue by inferred Service Category (Sec 2.2).

## {terms['risks_mitigation']}
*   [Identify 2-3 key risks **for {context_company_name}** based on the JSON analysis (e.g., revenue concentration in one service, declining trend, competition inferred from tags) and propose brief mitigation ideas for the {context_company_name} team.]
    *   Example: **Risk:** High concentration of won revenue in [Service X]. **Mitigation:** Develop targeted campaigns for identified white space areas [Area Y, Z] to diversify revenue stream.

## Final Struct Instructions:
Output the analysis report directly in **{language}** using **Markdown**. Do not include these instructions or conversational text. Ensure all sections (0-7) are generated according to the logic, handling the "No Won Deals" scenario correctly. Adhere strictly to formatting and constraints.
---
{formatted_completion_checks}
""" # End of main prompt f-string

    return prompt

# Example usage:
# company = "株式会社三越伊勢丹ホールディングス"
# context_company = "NESIC" # Or another name
# analysis_prompt_jp = get_analysis_prompt(company, language="Japanese", context_company_name=context_company)
# print(analysis_prompt_jp)
# analysis_prompt_en = get_analysis_prompt(company, language="English", context_company_name=context_company)
# print(analysis_prompt_en)