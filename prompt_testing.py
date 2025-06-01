import textwrap
from typing import Optional

# ADDITIONAL REFINED INSTRUCTIONS: Incorporates stronger measures for accuracy, table formatting, single-entity coverage, etc.
ADDITIONAL_REFINED_INSTRUCTIONS = textwrap.dedent("""\
    **Additional Refined Instructions for Zero Hallucination, Perfect Markdown, and Strict Single-Entity Coverage:**

    *   **Dedicated No-Output Fallback if Missing Sources:**
        1. If no valid Vertex AI grounding URLs exist for a required factual point or section, omit that data entirely (do not guess or fabricate).
        2. In the relevant subsection, explicitly state: "No verifiable data found [SSX], omitted due to missing official grounding."
        3. If a table is requested but data is unavailable, provide a placeholder row or empty table noting "No verifiable data found [SSX]."

    *   **Mandatory Self-Check Before Final Output:**
        - Before producing the final answer, confirm:
            1. All requested sections are fully included.
            2. All factual statements have inline citations [SSX] pointing to valid Vertex AI URLs in the final Sources list.
            3. Only the permitted Vertex AI grounding URLs are used—no external or fabricated links.
            4. Markdown headings and tables follow the specified format (##, ###, consistent columns).
            5. A single "Sources" section is present, properly labeled, and each source is on its own line.
            6. Inline citations appear before punctuation where feasible.
            7. No data or sources are invented.
            8. Strictly reference only the exact named company; do not include similarly named entities.

    *   **Exactness of Table Columns:**
        - Each row in any table must have the same number of columns as the header row.
        - If data is missing, insert "-" or "(No Data)" but keep the columns aligned.
        - Always include an inline citation if referencing factual numbers.

    *   **Quotes with Inline Citations:**
        - Any verbatim quote must include:
            1. The speaker's name and date or document reference in parentheses.
            2. An inline citation [SSX] immediately following.
        - This ensures clarity on who said it, when they said it, and the exact source.

    *   **Exactness of Hyperlinks in Sources:**
        - The final "Sources" section must use the format "* [Supervity Source X](Full_URL) - Brief annotation [SSX]."
        - Number sources sequentially without skipping.
        - Provide no additional domain expansions or transformations beyond what is given.
        - Do not summarize entire documents—only note which facts the source supports.

    *   **Do Not Summarize Sources:**
        - In each source annotation, reference only the specific claim(s) the link supports, not a broad summary.

    *   **Placeholders for Non-Public Data:**
        - If certain requested info cannot be verified, omit it entirely or label it succinctly as "(No Public Data Found) [SSX]."
        - Maintain consistent formatting in either case.

    *   **High-Priority Checklist (Must Not Be Violated):**
        1. No fabrication: Omit rather than invent ungrounded data.
        2. Adhere strictly to the specified Markdown formats (headings, lists, tables).
        3. Use inline citations [SSX] matching final sources exactly.
        4. Provide only one "Sources" section at the end.
        5. Do not use any URLs outside "vertexaisearch.cloud.google.com/..." pattern if not explicitly provided.
        6. Enforce single-entity coverage: if "Marvel Inc." is the focus, do not include other similarly named entities.
        7. Complete an internal self-check to ensure compliance with all instructions before concluding.
""")

# FINAL SOURCE LIST INSTRUCTIONS: Revised to require inline citation linkage.
FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE = textwrap.dedent("""\
    **Final Source List Requirements:**

    Conclude the *entire* research output, following the 'General Discussion' paragraph, with a clearly marked section titled "**Sources**". This section is critical for verifying the information grounding process AND for document generation.

    **1. Content - MANDATORY URL Type & Source Integrity:**
    *   **Exclusive Source Type:** This list **MUST** contain *only* the specific grounding redirect URLs provided directly by the **Vertex AI Search system** *for this specific query*. These URLs represent the direct grounding evidence used.
    *   **URL Pattern:** These URLs typically follow the pattern: `https://vertexaisearch.cloud.google.com/grounding-api-redirect/...`. **Only URLs matching this exact pattern are permitted.**
    *   **Strict Filtering:** Absolutely **DO NOT** include any other type of URL (direct website links, news, PDFs, etc.).
    *   **CRITICAL - No Hallucination:** **Under NO circumstances should you invent, fabricate, infer, or reuse `vertexaisearch.cloud.google.com/...` URLs** from previous queries or general knowledge if they were not explicitly provided as grounding results *for this query*. If a fact is identified but lacks a corresponding provided grounding URL, it must be omitted.
    *   **Purpose:** This list verifies the specific grounding data provided by Vertex AI Search for this request—not external knowledge or other URLs.

    **2. Formatting and Annotation (CRITICAL FOR PARSING):**
    *   **Source Line Format:** Present each source on a completely new line. Each line **MUST** start with a Markdown list indicator (`* ` or `- `) followed by the hyperlink in Markdown format and then its annotation.
    *   **REQUIRED Format:** 
        ```markdown
        * [Supervity Source X](Full_Vertex_AI_Grounding_URL) - Annotation explaining exactly what information is supported (e.g., supports CEO details and FY2023 revenue [SSX]).
        ```
    *   **Sequential Labeling:** The visible hyperlink text **MUST** be labeled sequentially "Supervity Source 1", "Supervity Source 2", etc. Do not skip numbers.
    *   **Annotation Requirement:** The annotation MUST be:
        * Included immediately after the hyperlink on the same line, separated by " - ".
        * Brief and specific, explaining exactly which piece(s) of information in the main body (and referenced with inline citation [SSX]) that grounding URL supports.
        * Written in the target output language: **{language}**.

    **3. Quantity and Linkage:**
    *   **Target Quantity:** Aim for a minimum of 5 and a maximum of 18 distinct, verifiable Vertex AI grounding URLs that directly support content in the report.
    *   **Accuracy Over Quantity:** Accuracy and adherence to the grounding rules are absolute. If fewer than 5 verifiable URLs are available from the provided results, list only those.
    *   **Fact Linkage:** Every grounding URL listed MUST directly correspond to facts/figures/statements present in the report body. The annotation must clearly link to the inline citation(s) [SSX] used in the text.

    **4. Content Selection Based on Verifiable Grounding:**
    *   **Prerequisite for Inclusion:** Only include facts, figures, details, or quotes in the main report if they can be supported by a verifiable Vertex AI grounding URL from this query.
    *   **Omission of Ungrounded Facts/Sections:** If specific information cannot be supported by a verifiable grounding URL, omit that detail. If a whole section cannot be grounded, omit the entire section.

    **5. Final Check:**
    *   Before concluding the response, review the entire output. Verify:
        * Exclusive use of valid, provided Vertex AI grounding URLs.
        * Each source is on a new line and follows the correct format.
        * Every fact in the report body is supported by an inline citation [SSX] that corresponds to a source in this list.
    *   The "**Sources**" section must appear only once, at the end of the entire response.
    """)

# HANDLING MISSING INFORMATION: Revised to enforce strict omission if grounding is unavailable.
HANDLING_MISSING_INFO_INSTRUCTION = textwrap.dedent("""\
    *   **Handling Missing or Ungrounded Information:**
        *   **Exhaustive Research First:** Conduct exhaustive research using primarily official company sources (see `RESEARCH_DEPTH_INSTRUCTION`).
        *   **Grounding Requirement for Inclusion:** Information is included only if:
            1. The information is located in a reliable source document.
            2. A corresponding, verifiable Vertex AI grounding URL (matching the pattern `https://vertexaisearch.cloud.google.com/grounding-api-redirect/...`) is provided in the search results for this query.
        *   **Strict Omission Policy:** If information cannot meet both conditions, omit that specific fact or section entirely. Do not use placeholders such as 'N/A' or 'Not Found'.
        *   **No Inference/Fabrication:** Do not infer, guess, or estimate ungrounded information. Do not fabricate grounding URLs.
        *   **Cross-Language Search:** If necessary, check other language results; if found, translate only the necessary information and list the corresponding grounding URL.
    """)

# RESEARCH DEPTH & CALCULATION: Revised to include forbidden sources and conflict handling.
RESEARCH_DEPTH_INSTRUCTION = textwrap.dedent("""\
    *   **Research Depth & Source Prioritization:**
        *   **Exhaustive Search:** Conduct thorough research for all requested information points. Dig beyond surface-level summaries.
        *   **Primary Source Focus:** Use official company sources primarily, including:
            * Latest Annual / Integrated Reports (and previous years for trends)
            * Official Financial Statements (Income Statement, Balance Sheet, Cash Flow) & Crucially: Footnotes
            * Supplementary Financial Data, Investor Databooks, Official Filings (e.g., EDINET, SEC filings, local equivalents)
            * Investor Relations Presentations & Materials (including Mid-Term Plans, Strategy Day presentations)
            * Earnings Call Transcripts & Presentations (focus on Q&A sections)
            * Official Corporate Website sections (e.g., "About Us", "Investor Relations", "Strategy", "Governance", "Sustainability/ESG")
            * Official Press Releases detailing strategy, financials, organizational structure, or significant events.
        *   **Forbidden Sources:** Do NOT use:
            * Wikipedia
            * Generic blogs, forums, or social media posts
            * Press release aggregation sites (unless linking directly to an official release)
            * Outdated market reports (unless historical context is explicitly requested)
            * Competitor websites/reports (except in competitive analysis with caution)
            * Generic news articles unless they report specific, verifiable events from highly reputable sources (e.g., Nikkei, Bloomberg, Reuters, FT, WSJ).
        *   **Emphasize Primary Sources:** Primary documents provide accuracy, official positioning, and verifiability.
        *   **Management Commentary:** Actively incorporate direct management commentary and analysis from these sources.
        *   **Recency:** Focus on the most recent 1-2 years for qualitative analysis; use the last 3 full fiscal years for financial trends. Clearly state the reporting period.
        *   **Secondary Sources:** Use reputable secondary sources sparingly for context or verification, always with clear attribution.
        *   **Handling Conflicts:** If conflicting information is found between official sources, prioritize the most recent, definitive source. Note discrepancies with dual citations if significant (e.g., [SSX, SSY]).
        *   **Calculation Guidelines:** If metrics are not explicitly reported but must be calculated:
            * Calculate only if all necessary base data (e.g., Net Income, Revenue, Equity, Assets, Debt) is available and verifiable.
            * Clearly state the formula used, and if averages are used, mention that.
        *   **Confirmation of Unavailability:** Only conclude information is unavailable after a diligent search across multiple primary sources.
    """)

# ANALYSIS & SYNTHESIS INSTRUCTION: Revised to encourage explicit "why" analysis and linking.
ANALYSIS_SYNTHESIS_INSTRUCTION = textwrap.dedent("""\
    *   **Analysis and Synthesis:**
        *   Beyond listing factual information, provide concise analysis where requested (e.g., explain trends, discuss implications, identify drivers, assess effectiveness).
        *   **Explicitly address "why":** For every data point or trend, explain why it is occurring or what the key drivers are.
        *   **Comparative Analysis:** Compare data points (e.g., YoY changes, company performance against competitors) where appropriate.
        *   **Linking Information:** In the General Discussion, explicitly tie together findings from different sections to present a coherent overall analysis (e.g., link financial performance with strategic initiatives).
    """)

# INLINE CITATION INSTRUCTION: Mandate inline citations for all factual claims.
INLINE_CITATION_INSTRUCTION = textwrap.dedent("""\
    *   **Inline Citation Requirement:**
        *   Every factual claim, data point, and specific summary must include an inline citation in the format [SSX], where X corresponds exactly to the sequential number of the source in the final Sources list.
        *   Place the inline citation immediately after the supported statement and before punctuation when possible.
        *   If a single source supports multiple facts, reuse the same [SSX].
        *   This ensures that each fact is directly verifiable against the corresponding "Supervity Source X" in the final Sources list.
    """)

# SPECIFICITY INSTRUCTION: Instruct to include specific dates, definitions, and quantification.
SPECIFICITY_INSTRUCTION = textwrap.dedent("""\
    *   **Specificity and Granularity:**
        *   For all time-sensitive data points (e.g., financials, employee counts, management changes), include specific dates or reporting periods (e.g., "as of 2024-03-31", "for FY2023").
        *   Define any industry-specific or company-specific terms or acronyms on their first use.
        *   Quantify qualitative descriptions with specific numbers or percentages where available (e.g., "growth of 12% [SSX]").
        *   List concrete examples rather than vague categories when describing initiatives, strategies, or risks.
    """)

# AUDIENCE CONTEXT REMINDER
AUDIENCE_CONTEXT_REMINDER = textwrap.dedent("""\
    *   **Audience Relevance:** Keep the target audience (Japanese corporate strategy professionals) in mind. Frame analysis and the 'General Discussion' to highlight strategic implications, competitive positioning, market opportunities/risks, and operational insights relevant for potential partnership, investment, or competitive assessment.
    """)

# ANALYZING COMPANY CAPABILITIES INSTRUCTION: Mandatory research and application of context company capabilities
ANALYZING_COMPANY_CAPABILITIES_INSTRUCTION = textwrap.dedent("""\
    **MANDATORY: Analyzing Company ({context_company_name}) Capabilities Research & Application**

    Before creating any strategic recommendations, you MUST conduct exhaustive research on the **Analyzing Company ({context_company_name})** to understand its specific capabilities, solutions, and competitive strengths. This research is essential for creating targeted, non-generic strategic alignments with the **Target Company ({company_name})**.

    **Required {context_company_name} Research Areas:**
    1. **Solution Portfolio Mapping**: Identify and catalog {context_company_name}'s specific named solutions, platforms, services, and offerings (e.g., "CloudSecure Platform", "AI Analytics Suite", "Digital Transformation Accelerator"). Do not use generic terms.
    
    2. **Industry Expertise & Verticals**: Determine {context_company_name}'s proven industry experience, vertical specializations, and sector-specific solutions that may align with {company_name}'s industry.
    
    3. **Technology Partnerships & Certifications**: Research {context_company_name}'s key technology partnerships (e.g., AWS Premier Partner, Microsoft Gold Partner), certifications, and ecosystem relationships that could be relevant to {company_name}'s technology environment.
    
    4. **Service Capabilities**: Identify {context_company_name}'s service delivery models (e.g., consulting, managed services, system integration, support models) and geographic service coverage.
    
    5. **Competitive Differentiators**: Research {context_company_name}'s unique value propositions, proven methodologies, proprietary tools, and competitive advantages in relevant market segments.
    
    6. **Case Studies & Success Stories**: Look for relevant client success stories, case studies, or proven implementations that demonstrate {context_company_name}'s capabilities in similar contexts to {company_name}.

    **Application Requirements:**
    *   **Specific Solution Alignment**: For every strategic recommendation, explicitly link {context_company_name}'s specific, named solutions to {company_name}'s verified needs, initiatives, or challenges.
    
    *   **Non-Generic Recommendations**: Avoid generic statements like "cloud services" or "digital transformation." Instead, reference specific {context_company_name} offerings like "SecureCloud Migration Framework" or "Industry-Specific AI Platform."
    
    *   **Competitive Positioning**: Leverage {context_company_name}'s researched strengths to position against known competitors in {company_name}'s environment.
    
    *   **Value Proposition Clarity**: Clearly articulate why {context_company_name}'s specific capabilities are uniquely suited to address {company_name}'s particular situation, not just general market needs.

    **Critical Success Factors:**
    *   Every strategic opportunity identified must demonstrate clear alignment between {context_company_name}'s actual, researched capabilities and {company_name}'s verifiable business situation.
    *   Recommendations must be actionable and specific, referencing actual {context_company_name} solutions and services.
    *   The analysis must position {context_company_name} as a strategic partner with differentiated value, not as a generic vendor.
    """)

# STANDARD OUTPUT LANGUAGE INSTRUCTION
def get_language_instruction(language: str) -> str:
    return f"Output Language: The final research output must be presented entirely in **{language}**. Make sure the sources are in {language}. If you do not find the sources in {language}, you can translate the content from the sources to {language} to use in the report, and then list the original source in the sources list."

# BASE_FORMATTING_INSTRUCTIONS: Revised to include logical flow and conciseness.
BASE_FORMATTING_INSTRUCTIONS = textwrap.dedent("""\
    Output Format & Quality Requirements:

    *   **Direct Start & No Conversational Text:** Begin the response directly with the first requested section heading (e.g., `## 1. Core Corporate Information`). No introductory or concluding remarks are allowed.
    
    *   **Strict Markdown Formatting Requirements:**
        *   Use valid and consistent Markdown throughout the entire document.
        *   **Section Formatting:** Sections MUST be numbered exactly as specified in the prompt (e.g., `## 1. Core Corporate Information`).
        *   **Subsection Formatting:** Use `###` for subsections and maintain hierarchical structure (e.g., `### CEO Name, Title`).
        *   **List Formatting:** Use asterisks (`*`) or hyphens (`-`) for bullets with consistent indentation (4 spaces for sub-bullets).
        *   **Tables:** Format all tables with proper Markdown table syntax:
            ```markdown
            | Header 1 | Header 2 | Header 3 |
            |----------|----------|----------|
            | Data 1   | Data 2   | Data 3   |
            | Data 4   | Data 5   | Data 6   |
            ```
        *   **Code Blocks:** Use triple backticks (```) for code blocks when presenting technical details.
        *   **Quotes:** Use Markdown quote syntax (>) for direct quotations from executives when appropriate.
    
    *   **Optimal Structure & Readability:**
        *   Present numerical data in tables with proper alignment and headers.
        *   Use bullet points for lists of items or characteristics.
        *   Use paragraphs for narrative descriptions and analysis.
        *   Maintain consistent formatting across similar elements throughout the document.
        *   **Content Organization:** Ensure a logical sequence within each section (e.g., chronological order for trends, priority order for lists).
        *   **Conciseness:** Provide detailed yet concise language—be specific without unnecessary verbosity.
    
    *   **Data Formatting Consistency:**
        *   Use appropriate thousands separators for numbers per the target language: **{language}**.
        *   **Currency Specification:** Always specify the currency (e.g., ¥, $, €, JPY, USD, EUR) for all monetary values along with the reporting period.
        *   Format dates in a consistent style (e.g., YYYY-MM-DD).
        *   Use consistent percentage formatting (e.g., 12.5%).
    
    *   **Table Consistency Requirements:**
        *   All tables must have header rows with clear column titles.
        *   Include a separator row (|---|---|) between headers and data.
        *   Align column content appropriately (left for text, right for numbers).
        *   Maintain the same number of columns throughout each table.
        *   Include units in column headers where applicable (e.g., "Revenue (JPY millions)").
    
    *   **Section Completion Verification:**
        *   Every section requested in the prompt MUST be included in the output.
        *   Sections must appear in the exact order specified in the prompt.
        *   Each section must be properly labeled with the exact heading from the prompt.
        *   Incomplete sections should be explicitly marked as having partial data rather than omitted entirely.
    
    *   **Tone and Detail Level:**
        *   Maintain a professional, objective, and analytical tone suited for a Japanese corporate strategy audience.
        *   Provide granular detail (e.g., figures, dates, metrics) while avoiding promotional language.
    
    *   **Completeness and Verification:**
        *   Address all requested points in each section.
        *   Verify that every section, the General Discussion, and the Sources list are present and adhere to the instructions.
        *   Perform a final internal review before output.

    *   **Sources List:** The Sources list must be present and adhere to the instructions.
        *   The Sources section should have a header with the text "Sources"
        *   The Sources section should be formatted as a Markdown unordered list.
        *   The Sources section should have a link to the source with the text "Source X" where X is the source number.
                                               
    *   **Inline Citation & Specificity:** Incorporate the inline citation [SSX] for every factual claim (see Inline Citation Requirement) and include specific dates/definitions (see Specificity and Granularity).
    """)

# FINAL REVIEW INSTRUCTION
FINAL_REVIEW_INSTRUCTION = textwrap.dedent("""\
    *   **Internal Final Review:** Before generating the 'Sources' list, review your generated response for:
    
        *   **Completeness Check:**
            * Every numbered section requested in the prompt is present
            * Each section contains all requested subsections and information points
            * The "General Discussion" paragraph is included
            * No sections have been accidentally omitted or truncated
        
        *   **Formatting Verification:**
            * All line breaks are properly formatted
            * All section headings use correct Markdown format (`## Number. Title`)
            * All subsections use proper hierarchical format (`###` or indented bullets)
            * Tables have proper headers, separators, and consistent columns
            * Lists use consistent formatting and indentation
        
        *   **Citation Integrity:**
            * Every factual claim has an inline citation [SSX]
            * Citations are placed immediately after the supported claim
            * All citations correspond to entries in the final Sources list
        
        *   **Data Precision:**
            * All monetary values specify currency and reporting period
            * All dates are in consistent format
            * Numerical data is presented with appropriate precision and units
        
        *   **Content Quality:**
            * Direct start with no conversational text
            * Professional tone with no placeholders or ambiguous statements
            * Adherence to missing info handling instructions
            * Logical flow within and between sections
        
        *   **Single-Entity Coverage:**
            * Ensure that only the specified company name is used and no similarly named entities are included unless they are verifiably the same entity.
        
        Proceed to generate the final 'Sources' list only after confirming these conditions are met.
    """)

# Template for ensuring complete and properly formatted output
COMPLETION_INSTRUCTION_TEMPLATE = textwrap.dedent("""\
    **Output Completion Requirements:**
    
    Before concluding your response, verify that:
    1. Every numbered section requested in the prompt is complete with all required subsections
    2. All content follows proper markdown formatting throughout
    3. Each section contains all necessary details and is not truncated
    4. The response maintains consistent formatting for lists, tables, and code blocks
    5. All inline citations [SSX] are properly placed, with no extraneous or fabricated URLs
    6. Strictly focus on the exact named company (no confusion with similarly named entities)
""")
# Basic Prompt
def get_basic_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for a comprehensive basic company profile with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f"""
**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Absolutely DO NOT include information about any other similarly named companies (e.g., entertainment, unrelated industries). Verify the identity of the company for all sourced information.

# Comprehensive Corporate Profile, Strategic Overview, and Organizational Analysis of {company_name}

## Executive Summary

This comprehensive corporate analysis provides a detailed examination of **{company_name}** covering core business operations, organizational structure, market positioning, and strategic outlook. The report synthesizes official company information, recent performance data, and leadership perspectives to deliver actionable insights for strategic decision-making. Key focus areas include corporate governance, competitive dynamics, management philosophy, and growth opportunities within the current market environment.

Objective: To compile a detailed, accurate, and analytically contextualized corporate profile, strategic overview, organizational structure analysis, and key personnel identification for {company_name}, focusing solely on this entity: {context_str}. Avoid detailed analysis of parent or subsidiary companies except for listing subsidiaries as requested and clearly sourced [SSX].

Target Audience Context: {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct in-depth research using {company_name}'s official sources. Perform exhaustive checks across multiple primary sources before omitting any requested information silently. Every factual claim, data point, and summary must include an inline citation in the format [SSX]. Provide specific dates or reporting periods (e.g., "as of 2025-03-31", "for FY2024"). Ensure every claim is grounded by a verifiable Vertex AI grounding URL referenced back in the final Sources list for **{company_name}**. Use the absolute latest available official information.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth}
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Company Overview**: Provide a concise 200-300 word executive summary highlighting the most critical findings about **{company_name}** [SSX]
*   **Key Strategic Insights**: Identify the 3-5 most significant strategic insights from your analysis [SSY]
*   **Business Position Assessment**: Summarize {company_name}'s current market position, competitive strengths, and key challenges [SSZ]
*   **Strategic Implications**: Highlight actionable implications for strategic decision-making and business development [SSW]
*   **Priority Recommendations**: List 2-3 priority recommendations or areas requiring attention [SSV]

## 1. Core Corporate Information:
    *   **Stock Ticker Symbol / Security Code**: (if publicly traded, verify it matches '{ticker or "N/A"}') [SSX]
    *   **Primary Industry Classification**: (e.g., GICS, SIC – specify the standard, verify it aligns with '{industry or "N/A"}') [SSX]
    *   **Full Name and Title of Current CEO**: [SSX] (Verify against latest official sources)
    *   **Full Registered Headquarters Address**: [SSX]
    *   **Main Corporate Telephone Number**: [SSX]
    *   **Official Corporate Website URL**: [SSX]
    *   **Date of Establishment/Incorporation**: (e.g., "established on YYYY-MM-DD") [SSX]
    *   **Date of Initial Public Offering (IPO)/Listing**: (if applicable, include exact date) [SSX]
    *   **Primary Stock Exchange/Market where listed**: (if applicable) [SSX]
    *   **Most Recently Reported Official Capital Figure**: (specify currency and reporting period, verify against latest financial statement/filing) [SSX]
    *   **Most Recently Reported Total Number of Employees**: (include reporting date and source; quantify any significant changes YoY if available [SSY]) [SSX]
    *   *Summary Paragraph*: Briefly summarize the company's situation based on the figures above, incorporating quantitative trends where available (e.g., "Capital increased by X% in the latest period...") [SSX].

## 2. Recent Business Overview:
    *   Provide a detailed summary of **{company_name}**'s core business operations and primary revenue streams based on the most recent official reports [SSX]. Include specific product or service details and any recent operational developments (with exact dates or periods).
    *   Include key highlights of recent business performance (e.g., "revenue increased by 12% in FY2024 [SSX]") or operational changes (e.g., restructuring, new market entries with dates), and explain their significance [SSX].

## 3. Business Environment Analysis:
    *   Describe the current market environment by identifying major competitors and market dynamics (include specific names, market share percentages if available and verifiable, and exact data dates as available [SSX]).
    *   Identify and explain key industry trends (e.g., technological shifts, regulatory changes) including specific figures or percentages where possible [SSX]. Note where these trends are discussed in company reports [SSY].
    *   ***Discuss the strategic implications and opportunities/threats these trends pose for {company_name} from a Japanese corporate perspective [SSX].***

## 4. Organizational Structure Overview:
    *   Describe the high-level organizational structure as stated in official sources (e.g., "divisional based on Mobility, Safety, and Entertainment sectors [SSX]", "functional", "matrix") and reference the source (e.g., "as shown in the Annual Report 2025, p. XX") [SSX].
    *   If an official organization chart is found in sources, note its existence and location (e.g., "An org chart is available on the company website under 'About Us' [SSX]" or "Figure X in the Annual Report [SSY] shows the structure.").
    *   Briefly comment on the rationale behind the structure (if stated) and its potential implications for decision-making and agility [SSX].

## 5. Key Management Personnel & Responsibilities:
    *   **Prioritize the latest official company website** for the most current lists of Directors and Executive Officers. Cross-reference with recent Annual Reports or official filings for verification and responsibilities. Ensure names/titles relate specifically to **{company_name}**, not exclusively a parent company unless specified.
    *   Present the Board of Directors and Audit & Supervisory Board members (or equivalent) in **perfectly formatted Markdown tables**. Include Name, Title, Key Notes (e.g., External, Committee Chair, Independence status), and Source(s). State the 'as of' date clearly for the data. Use '-' for missing data points only if needed for table structure. Ensure the *complete list* as per the source is included.
        *   **Board of Directors (as of 2025-03-31 [SSX])**:
            | Name | Title | Notes | Source(s) |
            |------|-------|-------|-----------|
            |      |       |       |           |
        *   **Audit & Supervisory Board Members / Equivalent (as of 2025-03-31 [SSX])**:
            | Name | Title | Notes | Source(s) |
            |------|-------|-------|-----------|
            |      |       |       |           |
    *   **Executive Officers (Management Team)**: List key members (beyond CEO) with titles and detailed descriptions of their strategic responsibilities (e.g., COO Mobility, CFO, CTO, Head of Administration). Include start dates or tenure if available [SSX]. Ensure the *complete list* as per the source is included. Use a list or table for clarity.

## 6. Subsidiaries List:
    *   List *major* direct subsidiaries (global where applicable) based solely on official documentation (e.g., list in Annual Report Appendix). Acknowledge this may not be exhaustive. For each subsidiary, include primary business activity, country of operation, and, if available, ownership percentage as stated in the source [SSX]. Present this in a **perfectly formatted Markdown table** for clarity. Use '-' for missing data points only if needed for table structure.
        
        **Example subsidiaries table format (replace with actual data)**:
        
        | Subsidiary Name       | Primary Business       | Country | Ownership % (if stated) | Source(s) |
        |-----------------------|------------------------|---------|-------------------------|-----------|
        | Example Subsidiary A  | Cloud Services         | Japan   | 100%                    | [SS1]     |
        | Example Subsidiary B  | AI Solutions           | USA     | 80%                     | [SS2]     |
        | Example Subsidiary C  | Consulting & Integration| UK      | -                       | [SS3]     |
        
        **NOTE: This empty table should be filled with actual verified subsidiaries of {company_name} from official sources, not fictional examples**:

## 7. Leadership Strategic Outlook (Verbatim Quotes):
    *   **CEO & Chairman**: Provide at least four direct, meaningful quotes focusing on long-term vision, key challenges, growth strategies, and market outlook. Each quote must be followed immediately by its source citation in parentheses (e.g., "(Source: Annual Report 2025, p.5)"), and an inline citation [SSX] must confirm the quote's origin.
    
        **Example quote format**:
        
        > "Our strategic vision for the next five years focuses on expanding our digital capabilities while maintaining our commitment to sustainability." [SSX]
        > (Source: Annual Report 2025, p.5)
        
    *   **Other Key Executives (e.g., CFO, CSO, CTO, COO, relevant BU Heads)**: Provide verifiable quotes (aim for 1-3 per relevant executive if strategically insightful) detailing their perspective on their area of responsibility (e.g., financial strategy, tech roadmap, operational plans) with similar detailed attribution and inline citation [SSX].

## 8. General Discussion:
    *   Provide a concluding single paragraph (approximately 300-500 words).
    *   **Synthesize** the key findings exclusively from Sections 1-7 about **{company_name}**, explicitly linking analysis (e.g., "The organizational structure described in section 4 [SSX] supports the strategic focus mentioned by the CEO [SSY]...") and ensuring every claim is supported by an inline citation. Incorporate key quantitative points.
    *   Structure your analysis logically by starting with an overall assessment, then discussing strengths and opportunities, followed by weaknesses and risks, and concluding with an outlook relevant for the Japanese audience. Look for and mention potential DX implications arising from the company's structure or leadership messages [SSX].
    *   **Do not introduce new factual claims** that are not derived from the previous sections about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: All information must be factually correct, current, and verifiable against grounded sources for **{company_name}**. Specify currency and reporting periods for all monetary data. Omit unverified data silently after exhaustive search. Verify management lists against latest website data.
*   **Source Specificity (Traceability)**: Every data point, claim, and quote must be traceable to a specific source using an inline citation (e.g., [SSX]). These must match the final Sources list.
*   **Source Quality**: Use only official company sources primarily. Secondary sources may be used sparingly for context but must be verified and grounded. All sources must be clearly cited.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Financial Prompt
def get_financial_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for a detailed financial analysis with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    enhanced_financial_research_instructions = textwrap.dedent(f"""\
    *   **Mandatory Deep Search & Calculation**: Conduct an exhaustive search within **{company_name}**'s official financial disclosures for the last 3 full fiscal years, including Annual Reports, Financial Statements (Income Statement, Balance Sheet, Cash Flow Statement), **Footnotes**, Supplementary Data Packs (Databases, Tanshin), official filings, and IR materials. Do not rely solely on summary tables; examine detailed statements and notes for definitions and components [SSX]. Cross-verify figures across multiple sources. Verify table data accuracy meticulously. **Crucially, every single financial figure, ratio, or data point presented, whether in text or tables, MUST be directly supported by a verifiable Vertex AI grounding URL provided *for this query* [SSX] related to {context_str}.**
    *   **Time Period Clarity**: Always use the 3 most recently COMPLETED fiscal years with available data (e.g., FY2023, FY2024, FY2025). Clearly label the specific fiscal years in all tables and text (e.g., "FY2023, FY2024, FY2025" rather than just "last 3 years"). Include end dates where appropriate (e.g., "FY2025 ending March 31, 2026").
    *   **Calculation Obligation & Citation**: For financial metrics such as Margins, ROE, ROA, Debt-to-Equity, and ROIC: if not explicitly stated, calculate them using standard formulas only if all necessary base data is available and verifiable from grounded sources for {company_name}. Clearly state the formula used [SSX]. **When reporting a calculated metric, cite the sources for all underlying base data points used in the calculation** (e.g., "ROE (Calculated: NI [SS1] / Avg Equity [SS2]) [SS1, SS2]").
    *   **Strict Silent Omission Policy**: If a metric cannot be found or reliably calculated from verifiable sources after exhaustive search, omit that specific line item entirely. Do not use placeholders like 'N/A' or state that data is missing.
    *   **Industry Specific Metrics**: Be aware of industry nuances (e.g., for Insurance, distinguish between flow metrics like 'premium income' and stock metrics like 'annualized premiums in-force' if both are reported and used strategically, e.g., in MTP targets). If including non-standard metrics, briefly explain their definition/relevance based on the source [SSX].
    *   **Data Sparsity Acknowledgement (Internal)**: For non-listed subsidiaries or complex groups, acknowledge internally that certain detailed metrics might be unavailable at the subsidiary level and analysis will rely on available consolidated or segment data for {company_name}.
    *   **Missing Data Presentation**: In tables, use a single hyphen ('-') as a placeholder ONLY when needed for table structure, and ONLY when you've confirmed the data is genuinely missing in the source after thorough searching. DO NOT use 'N/A', blank cells, or explanatory text in table cells.
    """)

    analytical_depth_instructions = textwrap.dedent("""\
    *   **Analytical Depth Requirements**:
        *   **Time-Series Trends**: For key metrics of {company_name}, identify and analyze growth/decline trends over the 3-year period. Quantify these trends (e.g., CAGR, YoY change) [SSX]. Explain the *drivers* behind these trends using management commentary or related data (e.g., cost structure changes impacting margins) [SSY].
        *   **Competitive Comparison Outliers (if feasible)**: If reliable, grounded data for key competitors (identified in separate competitive analysis) is available, identify metrics where {company_name} appears unusually high or low (e.g., high fixed cost ratio, lower ROA than industry average). Analyze potential reasons based on sources [SSX, SSY]. *Perform this only if competitor data is grounded and available.*
        *   **Management Efficiency Evaluation**: Objectively evaluate management efficiency of {company_name} using relevant ratios (ROE, ROA, Margins, etc.) compared to past performance and targets [SSX].
        *   **Causal & Correlation Analysis**: Analyze potential correlations (e.g., sales vs. advertising costs, operating profit vs. personnel costs) based on reported data and management discussion for {company_name} [SSX]. Identify key drivers impacting profitability (e.g., "Which KPI is working for profit?" based on segment data or management statements) [SSY].
        *   **Identify Key Management Drivers**: Based on the analysis of {company_name}, highlight the primary levers management appears to be using or focusing on to influence financial performance [SSX].
    """)

    advanced_analysis_feasibility_note = textwrap.dedent(f"""\
    *   **Advanced Analysis (Feasibility Dependent)**: If sufficient historical and competitive data is available and grounded, attempt the following:
        *   **Competitor Comparison Matrix**: Create a matrix comparing key financial metrics (from Section 2) between {company_name} and 1-2 key competitors for the latest year [SSX, SSY]. *Only if grounded competitor data is available.*
        *   **Financial Soundness Risk Scoring**: (Conceptual) Briefly assess {company_name}'s financial soundness based on key ratios (leverage, liquidity, profitability trends). *Do not create a numerical score unless a published methodology is cited [SSX].*
        *   **Scenario Analysis / Forecasting**: (Conceptual) Summarize any company-provided forecasts or scenarios for {company_name} (e.g., MTP targets, sensitivity analysis like FX impact mentioned in reports [SSX]). *Do not perform independent forecasting.* Briefly describe forecasting models mentioned in sources if any [SSY].
    """)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Absolutely DO NOT include information about any other similarly named companies. Verify the identity for all financial data sourced.

# Comprehensive Strategic Financial Analysis of {company_name} (Last 3 Fiscal Years)

## Executive Summary

This detailed financial analysis examines **{company_name}**'s performance across the most recent three fiscal years, providing comprehensive insights into profitability, financial position, cash flows, and operational efficiency. The report combines quantitative analysis with strategic context to assess financial health, identify key performance drivers, and evaluate management effectiveness. Analysis includes trend identification, competitive positioning, and risk assessment to support strategic planning and investment decisions.

Objective: Deliver a complete, analytically rich, and meticulously sourced financial profile of **{company_name}** using the last three full fiscal years. Combine traditional financial metrics with analysis of profitability, cost structure, cash flow, investments, and contextual factors. Provide deep analysis explaining trends and drivers, requiring meticulous sourcing and in-depth analysis explaining the 'why' behind the numbers. Focus strictly on {context_str}.

Target Audience Context: This analysis is for a **Japanese corporate strategy audience**. Use Japanese terminology when appropriate (e.g., "売上総利益" for Gross Profit) and ensure that all monetary values specify currency (e.g., JPY millions) and reporting period (e.g., "FY2024 ended March 31, 2025") with exact dates where available [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
For each section, provide verifiable data with inline citations [SSX] and specific dates or reporting periods after conducting exhaustive research across multiple primary sources (including **footnotes**) for **{company_name}**. **Every single financial figure MUST have a verifiable grounding URL citation [SSX] from this query.** Every claim must be traceable to a final source. Silently omit any data not found. Use **perfect Markdown tables** for financial data presentation, verifying data accuracy against sources. Use '-' for missing data points only if needed for table structure. *Consider adding industry-specific metrics if relevant and reported (see instructions).*
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth}
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{enhanced_financial_research_instructions}
{ANALYSIS_SYNTHESIS_INSTRUCTION}
{analytical_depth_instructions}
{advanced_analysis_feasibility_note}

{formatted_additional_instructions}

## Executive Summary
*   **Financial Health Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s financial position and key trends [SSX]
*   **Critical Performance Indicators**: Highlight the 3-5 most significant financial metrics and their implications [SSY]
*   **Trend Analysis Summary**: Summarize key financial trends, growth patterns, and areas of concern over the analysis period [SSZ]
*   **Strategic Financial Insights**: Identify financial strengths, weaknesses, and strategic implications for stakeholders [SSW]
*   **Investment & Risk Assessment**: Provide key insights for investment decisions and risk evaluation [SSV]

## 1. Top Shareholders:
    *   List major shareholders of {company_name} (typically the top 5-10, with exact ownership percentages, reporting dates, and source references) in a **perfectly formatted Markdown table** [SSX]. Use '-' for missing data points only if needed for table structure.
        
        **Example shareholders table format (replace with actual data)**:
        
        | Shareholder Name        | Ownership % | As of Date   | Source(s) |
        |-------------------------|-------------|--------------|-----------|
        | Japan Trustee Services Bank | 10.2%       | 2024-03-31   | [SS1]     |
        | Custody Bank of Japan   | 8.5%        | 2024-03-31   | [SS2]     |
        | State Street Bank       | 6.1%        | 2024-03-31   | [SS3]     |
        
        **NOTE: "Japan Trustee Services Bank", "Custody Bank of Japan", etc. are illustrative examples. Replace with actual top shareholders of {company_name}**:
    *   Briefly comment on the stability or influence of the ownership structure on the financial strategy of {company_name} [SSX].

## 2. Key Financial Metrics (3-Year Trend in a Table):
    *   Present the following metrics for {company_name} for the last 3 full fiscal years (FY2023, FY2024, FY2025) in a **perfectly formatted Markdown table**. Specify currency (e.g., JPY millions) and fiscal year for each value. Verify data accuracy. If calculated, note this below the table or in a 'Notes' column and cite base data sources. Cite sources for all data [SSX]. Use '-' for missing data points only if needed for table structure. *Consider adding industry-specific metrics if relevant and reported (see instructions).*
        
        **Example financial metrics table format (replace with actual data)**:
        
        | Metric                                           | FY2023  | FY2024  | FY2025  | Notes / Calculation Basis | Source(s) |
        |--------------------------------------------------|---------|---------|---------|---------------------------|-----------|
        | Total Revenue / Net Sales / Premium Income etc.  | 123,456 | 135,789 | 142,853 | As reported               | [SS1]     |
        | Gross Profit                                     | 45,678  | 48,567  | 52,321  | Rev [SS1] - COGS [SS2]    | [SS1, SS2]|
        | Gross Profit Margin (%)                          | 37.0%   | 35.8%   | 36.6%   | GP [SS2] / Rev [SS1]      | [SS1, SS2]|
        | EBITDA                                           | 23,456  | 25,678  | 28,543  | As reported               | [SS3]     |
        | EBITDA Margin (%)                                | 19.0%   | 18.9%   | 20.0%   | EBITDA [SS3] / Rev [SS1]  | [SS1, SS3]|
        | Operating Income / Operating Profit              | 18,765  | 20,543  | 22,876  | As reported               | [SS1]     |
        | Operating Margin (%)                             | 15.2%   | 15.1%   | 16.0%   | OpInc [SS1] / Rev [SS1]   | [SS1]     |
        | Ordinary Income / Pre-Tax Income                 | 17,654  | 19,876  | 21,987  | As reported               | [SS2]     |
        | Ordinary Income Margin (%)                       | 14.3%   | 14.6%   | 15.4%   | OrdInc [SS2] / Rev [SS1]  | [SS1, SS2]|
        | Net Income attributable to Parent                | 12,345  | 14,567  | 15,678  | As reported               | [SS1]     |
        | Net Income Margin (%)                            | 10.0%   | 10.7%   | 11.0%   | NetInc [SS1] / Rev [SS1]  | [SS1]     |
        | ROE (%)                                          | 8.7%    | 9.5%    | 9.8%    | NI [SS1] / Avg Eq [SS4]   | [SS1, SS4]|
        | ROA (%)                                          | 4.3%    | 4.8%    | 5.0%    | NI [SS1] / Avg As [SS4]   | [SS1, SS4]|
        | Total Assets                                     | 245,678 | 267,890 | 285,430 | As reported               | [SS4]     |
        | Total Shareholders' Equity                       | 145,678 | 156,789 | 167,890 | As reported               | [SS4]     |
        | Equity Ratio (%)                                 | 59.3%   | 58.5%   | 58.8%   | Eq [SS4] / Assets [SS4]   | [SS4]     |
        | Total Interest-Bearing Debt                      | 45,678  | 48,765  | 50,123  | As reported               | [SS5]     |
        | Debt-to-Equity Ratio (x)                         | 0.31    | 0.31    | 0.30    | Debt [SS5] / Eq [SS4]     | [SS4, SS5]|
        | Net Cash from Operations                         | 24,567  | 26,789  | 28,976  | As reported               | [SS6]     |
        | Net Cash from Investing                          | -15,678 | -18,765 | -19,876 | As reported               | [SS6]     |
        | Net Cash from Financing                          | -7,654  | -8,765  | -9,876  | As reported               | [SS6]     |
        | (Add other key metrics like Premiums In-Force)    | -       | -       | -       |                           | [SSX]     |
    *   **Analyze** key trends observed in the table for {company_name} (YoY changes, CAGR). Explain the *drivers* behind these trends based on source commentary [SSX]. Identify any standout performance aspects (positive or negative) [SSY].

## 3. Profitability Analysis (3-Year Trend):
    *   Analyze trends in Operating Margin and Net Income Margin for {company_name} in more detail (building on the table above). Explain the *drivers* behind these trends (e.g., cost variations, pricing power, product mix shifts, one-off items mentioned in reports) with specific evidence and inline citations [SSX]. Quantify changes YoY. Discuss the sustainability of current profitability levels [SSY].

## 4. Segment-Level Performance (if applicable, Last 3 Fiscal Years):
    *   If segment data is available for {company_name} (e.g., Mobility, Safety, Entertainment), present revenue, operating profit, and margin percentages for each segment in a **perfectly formatted Markdown table** (include currency and fiscal year, verify data) [SSX]. Use '-' for missing data points only if needed for table structure.
        
        **IMPORTANT: The table below uses EXAMPLE SEGMENT NAMES AND FICTIONAL VALUES FOR ILLUSTRATION ONLY. Replace with actual segments and verified financial data from {company_name}'s reports**:
        
        | Segment Name        | Metric            | FY2023  | FY2024  | FY2025  | Source(s) |
        |---------------------|-------------------|---------|---------|---------|-----------|
        | Cloud Services      | Revenue (JPY M)   | 45,678  | 48,765  | 52,345  | [SS1]     |
        | Cloud Services      | Operating Income  | 7,654   | 8,123   | 8,765   | [SS1]     |
        | Cloud Services      | Operating Margin% | 16.8%   | 16.7%   | 16.7%   | [SS1]     |
        | AI Solutions        | Revenue (JPY M)   | 34,567  | 38,765  | 42,345  | [SS2]     |
        | AI Solutions        | Operating Income  | 5,678   | 6,123   | 7,654   | [SS2]     |
        | AI Solutions        | Operating Margin% | 16.4%   | 15.8%   | 18.1%   | [SS2]     |
        | Cybersecurity       | Revenue (JPY M)   | 15,678  | 16,543  | -       | [SS3]     |
        | Cybersecurity       | Operating Income  | 2,345   | 2,678   | -       | [SS3]     |
        | Cybersecurity       | Operating Margin% | 15.0%   | 16.2%   | -       | [SS3]     |
        
        **NOTE: "Cloud Services", "AI Solutions", "Cybersecurity" are placeholders. Use the actual segment names from {company_name}'s financial reports.**
    *   Analyze trends, growth drivers, and the relative contribution/profitability of each segment of {company_name}, citing specific figures [SSX]. Identify key profit-driving segments based on available data [SSY].

## 5. Cost Structure Analysis (3-Year Trend):
    *   Detail the composition and trends of major operating costs for {company_name} using data from financial statements [SSX]. Present in a **perfectly formatted Markdown table** if helpful and data is verifiable. Verify data accuracy. Use '-' for missing data points only if needed for table structure.
        
        **IMPORTANT: The table below contains FICTIONAL EXAMPLE COST DATA. Never use these specific amounts or percentages in your response. Replace with actual cost data from {company_name}'s financial reports.**
        
        | Cost Item           | FY2023 (JPY M) | FY2023 (% of Rev) | FY2024 (JPY M) | FY2024 (% of Rev) | FY2025 (JPY M) | FY2025 (% of Rev) | Source(s) |
        |--------------------|----------------|-------------------|----------------|-------------------|----------------|-------------------|-----------|
        | COGS               | 77,778         | 63.0%             | 87,222         | 64.2%             | 90,532         | 63.4%             | [SS1]     |
        | SG&A Expenses      | 27,111         | 22.0%             | 28,024         | 20.6%             | 29,444         | 20.6%             | [SS2]     |
        |  - R&D (if sep)    | 5,432          | 4.4%              | 6,120          | 4.5%              | 6,780          | 4.7%              | [SS3]     |
        |  - Personnel       | 8,600          | 7.0%              | 8,925          | 6.6%              | 9,100          | 6.4%              | [SS4]     |
        |  - Other SG&A      | 13,079         | 10.6%             | 12,979         | 9.6%              | 13,564         | 9.5%              | [SS5]     |
        
        **NOTE: All figures above are examples only. Your response must use actual cost data from {company_name}'s financial documents.**

## 6. Cash Flow Statement Analysis (3-Year Trend):
    *   Analyze trends in Operating Cash Flow (OCF) for {company_name}. Explain key drivers, differentiating between changes in profit and changes in working capital components (receivables, payables, inventory) based on the cash flow statement details [SSX].
    *   Detail major Investing Cash Flow activities (e.g., CapEx, acquisitions) and Financing Cash Flow activities (e.g., debt issuance/repayment, dividends, share buybacks) for {company_name} with specific amounts (specify currency) and context [SSX].
    *   Calculate and analyze Free Cash Flow (FCF = OCF - CapEx) trend for {company_name} [SSX]. Cite base data sources [SSY, SSZ]. Comment on the company's capacity to fund operations, investments, and shareholder returns based on FCF generation [SSW].

## 7. Investment Activities (Last 3 Years):
    *   Describe major M&A deals involving {company_name} (target, deal value if public, date, strategic rationale) [SSX].
    *   Analyze {company_name}'s capital expenditure (CapEx) patterns (total amount, key areas like factories/equipment/software) [SSY].
    *   Detail any significant corporate venture capital (CVC) or R&D investments by {company_name} with specific amounts (specify currency and reporting period) and stated goals [SSZ].
    *   Analyze the strategic rationale and potential financial impact (if commented on by management) of these investments for {company_name} [SSX, SSY, SSZ].

## 8. Contextual Financial Factors:
    *   Identify significant one-time events impacting {company_name} (e.g., asset sales, restructuring charges, impairment losses, litigation settlements) reported in the last 3 years, specifying dates, financial impacts (gain/loss in specified currency), and source notes [SSX].
    *   Discuss any significant accounting standard changes that impacted {company_name}'s reported figures during the period [SSY].
    *   Mention any key external economic or regulatory factors explicitly cited by {company_name}'s management as impacting financial performance [SSZ].
    *   Critically analyze the quality and sustainability of {company_name}'s reported earnings, considering the impact of one-time items and accounting choices noted [SSX, SSY, SSZ].

## 9. Credit Ratings & Financial Health (if available):
    *   List current and historical credit ratings for {company_name} from major agencies (e.g., S&P, Moody's, Fitch, R&I, JCR) with reporting dates [SSX].
    *   Summarize key highlights or concerns mentioned in the rating agencies' commentary regarding {company_name} [SSY].
    *   Analyze the implications of these ratings (or lack thereof) for {company_name}'s financial flexibility and cost of capital [SSX, SSY].

## General Discussion:
    *   Provide a concluding single paragraph (300-500 words) that synthesizes the findings exclusively from Sections 1-9 regarding **{company_name}**. Explicitly connect the analysis (e.g., "The strong cash flow generation [SSX] supports the investment strategy outlined in Section 7 [SSY], despite the margin pressure noted in Section 3 [SSZ]..."). Explain *why* trends are occurring based on the analysis. Incorporate key quantitative results. Discuss implications for future financial performance and strategic options for {company_name}.
    *   Structure the discussion logically by starting with an overall assessment of {company_name}'s financial health and performance trends, then discussing profitability drivers, cash flow adequacy, investment effectiveness, and concluding with an outlook (including strengths/weaknesses) tailored to a Japanese audience.
    *   Do not introduce any new factual claims that are not supported by previous sections and citations about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: All information must be current and verifiable for **{company_name}**. Specify currency (e.g., JPY millions) and reporting period (e.g., FY2024) for every monetary value. Silently omit unverified data after exhaustive search. Verify table data meticulously. **Every financial figure must have a grounding URL citation [SSX].**
*   **Source Specificity**: Every data point (in text, tables) must include an inline citation [SSX] that corresponds to a specific source in the final Sources list. Cite base data for calculations.
*   **Source Quality**: Rely primarily on official company sources for **{company_name}** (Financial Statements, Footnotes, Tanshin, IR Presentations, Annual Reports). Secondary sources may be used sparingly for context (like ratings) and must be clearly cited, verified, and grounded.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Competitive Landscape Prompt
def get_competitive_landscape_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for a detailed competitive analysis with nuanced grounding rules and expanded scope."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    competitive_research_instructions = textwrap.dedent(f"""\
    **Research & Grounding Strategy for Competitive Analysis**:

    1.  **Prioritize {company_name}'s Official Statements**: Use {company_name}'s own reports (Annual Report, IR materials) exhaustively to identify competitors *they* acknowledge [SSX] and their assessment of the market [SSY].
    2.  **Industry & Competitor Data Grounding**: For specific facts about the industry or competitors (e.g., market size/share, trends, competitor financials/products/strategies), use reliable third-party sources (reputable market research firms, financial news like Nikkei/Bloomberg, competitor's official reports) **only if** grounding URLs for these sources are provided by Vertex AI Search. Cite these using [SSY], [SSZ]. If no grounding URL is provided for an industry or competitor fact after exhaustive search, silently omit that specific data point. Do not invent facts or state unavailability. Ensure competitor data pertains to entities genuinely competing with {context_str}.
    3.  **Synthesis & Attribution**: When synthesizing competitive positioning or SWOT for {company_name}, clearly attribute claims. If based on {company_name}'s statements, use [SSX]. If based on grounded third-party data about the industry or a competitor, use [SSY], [SSZ]. Avoid unsourced analysis.
    4.  **Silent Omission Rule**: Silently omit any industry or competitor claim that cannot be traced back to either {company_name}'s statements [SSX] or a grounded third-party source [SSY, SSZ] after exhaustive search.
    5.  **Final Source List Integrity**: The final "Sources" list MUST include only the Vertex AI grounding URLs provided for this query (which may include links to {company_name}'s site or grounded third-party sites). Inline citations [SSX, SSY, SSZ] must match these sources.
    6.  **Timeframe Clarity**: For competitor and market data, always specify the exact timeframe (e.g., "As of FY2024" or "Data from Q2 2024") and ensure you're using the most recently available complete data. For trend analysis, specify the period covered (e.g., "Market share trends from 2022-2024 show...").
    7.  **Missing Data Handling**: In tables, use a single hyphen ('-') as a placeholder ONLY when needed for table structure and ONLY when you've confirmed the data is truly unavailable in reliable sources after thorough searching. DO NOT use 'N/A', blank cells, or explanatory text in table cells.
    """)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str} and its competitive landscape. Verify the identity of the company for all sourced information. Do not include unrelated entities.

# Detailed Competitive Analysis and Strategic Positioning of {company_name}

## Executive Summary

This competitive intelligence analysis examines **{company_name}**'s position within its industry ecosystem, identifying key competitors, market dynamics, competitive advantages, and strategic threats. The report provides comprehensive insights into market share positioning, competitive strengths and vulnerabilities, and strategic opportunities for competitive differentiation. Analysis focuses on actionable intelligence to support strategic planning and competitive positioning decisions.

Objective: To conduct a comprehensive competitive analysis of **{company_name}** including industry overview, competitor identification, analysis of their market presence and strategies, and an assessment of {company_name}'s own competitive positioning, strategy, and detailed capabilities. Conclusions should include a synthesized discussion relevant to a Japanese corporate audience. Focus strictly on {context_str}.

Target Audience Context: This output is for strategic review by a **Japanese company**. Ensure all analysis is supported by explicit inline citations [SSX] for {company_name}'s data/statements and [SSY, SSZ] for grounded industry/competitor data. Clearly attribute synthesized points. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Use **perfect Markdown tables**. Adhere strictly to grounding rules outlined below. Conduct exhaustive research before silently omitting unverified competitor or industry data. Use '-' for missing data points in tables only if needed for structure. Ensure all claims are verifiable.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on {company_name}'s view + grounded competitor/industry data
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{competitive_research_instructions}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Competitive Position Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s competitive landscape and market position [SSX]
*   **Key Competitive Advantages**: Identify the 3-5 most significant competitive strengths and differentiators [SSY]
*   **Market Dynamics Summary**: Summarize critical industry trends, competitive threats, and market opportunities [SSZ]
*   **Strategic Competitive Insights**: Highlight competitive positioning implications and strategic recommendations [SSW]
*   **Competitive Priorities**: List 2-3 priority areas for competitive enhancement or risk mitigation [SSV]

### 1. Industry Overview & Trends
    *   Describe the overall industry {company_name} operates in, aligning with '{industry or "N/A"}'. Include market size and growth rate estimates if verifiable data is available [SSY].
    *   Identify key technological, regulatory, economic, and social trends impacting the industry, citing sources [SSY, SSZ].
    *   Discuss the overall health and competitive intensity of the sector based on available grounded information [SSX, SSY].

### 2. Major Competitors Identification & Profiling
    *   Identify primary global and key regional competitors of {company_name} based on {company_name}'s official statements [SSX] or grounded third-party reports [SSY]. Provide specific names.
    *   Present competitor information in a **perfectly formatted Markdown table** where possible, clearly indicating source for each piece of data. Use '-' for missing data points only if needed for table structure. Verify data accuracy.
        
        **Example competitors table format (replace with actual data)**:
        
        | Competitor Name    | Primary Business Area(s) of Overlap with {company_name} | Estimated Market Share (Market, Year) | Key Geographic Overlap | Recent Key Moves (Date) | Source(s) |
        |--------------------|----------------------------------------------------------|---------------------------------------|------------------------|-------------------------|-----------|
        | IT Solutions Inc.  | Cloud Services, IT Consulting                            | 15.2% (Cloud Market, 2024) [SS1]      | Japan, SE Asia [SS2]   | Acquired AI Firm (2024-05) [SS3] | [SS1, SS2, SS3] |
        | Global Network Corp| Network Solutions, Security                              | 8.7% (Security Market, 2024) [SS4]    | Global [SS2]           | Launched Platform X (2023-11) [SS5] | [SS2, SS4, SS5] |
        | Tech Infra Ltd.    | IT Infrastructure                                        | -                                     | EMEA, APAC [SS2]       | New CEO appointed (2024-09) [SS6]   | [SS2, SS6]      |
        
        **NOTE: "IT Solutions Inc.", "Global Network Corp", etc. are illustrative examples. Replace with actual competitor names of {company_name}. All market share figures, geographic data, and key moves must be verified from reliable sources.**
    *   For key competitors identified, briefly analyze their relative positioning versus {company_name} on dimensions like technology, product range, price point, or regional strength, based *only* on grounded data [SSX, SSY]. Note strategic weaknesses if explicitly mentioned in sources [SSZ].

### 3. {company_name}'s Competitive Positioning
    *   **Strengths**: Detail {company_name}'s key competitive strengths as stated in official documents or evidenced by data (e.g., strong R&D pipeline [SSX], market leadership in Segment Y [SSY]). Provide specific examples.
    *   **Weaknesses**: Detail {company_name}'s potential competitive weaknesses or challenges acknowledged in official sources or implied by data (e.g., high cost structure compared to peers [SSX], dependence on a single market [SSY]).
    *   **Opportunities**: Identify potential opportunities for {company_name} arising from industry trends (from Section 1) or competitor weaknesses (from Section 2), based on grounded analysis [SSX, SSY].
    *   **Threats**: Identify potential threats to {company_name} arising from industry trends, competitor actions, or regulatory changes, based on grounded analysis [SSX, SSY].
    *   **Competitive Advantages**: Summarize {company_name}'s key sources of sustainable competitive advantage as stated or evidenced (e.g., proprietary technology [SSX], brand loyalty metrics [SSY], scale economies [SSZ]).

### 4. {company_name}'s Detailed Profile (Competitive Lens)
    *   **Products and Services**:
        *   Describe {company_name}'s main products/services and product line-up details [SSX].
        *   Discuss typical price range or positioning (e.g., premium, value) if stated [SSY].
        *   Highlight key quality/differentiation points mentioned in reports [SSZ].
        *   Comment on product development capabilities (e.g., frequency of new launches mentioned [SSX], R&D focus areas [SSY]).
        *   Mention track record/case studies if highlighted (especially for B2B) [SSZ].
    *   **Marketing and Sales Strategies**:
        *   Describe {company_name}'s primary sales channels (e.g., direct, EC, distributors) [SSX].
        *   Outline promotion strategies mentioned (advertising focus, SNS campaigns, etc.) [SSY].
        *   Summarize reported brand image or perception for {company_name} [SSZ].
        *   Note any mention of SEO/SNS utilization [SSX].
        *   Describe the customer support system if detailed [SSY].
    *   **Technological and Development Capabilities**:
        *   List any claimed patents or unique technologies for {company_name} [SSX].
        *   Report R&D expenditure trends (absolute and % of revenue if available) for {company_name} [SSY].
        *   Identify key development bases or centers for {company_name} [SSZ].
        *   Detail significant external collaborations (universities, research institutions, other companies) mentioned for {company_name} [SSX].
    *   **Other Relevant Factors (if information available for {company_name})**:
        *   Key aspects of Human Resources strategy mentioned (recruitment policy, training systems) [SSX].
        *   Reported Customer Satisfaction (CSAT/NPS) scores or word-of-mouth evaluations [SSY].
        *   Mention of external evaluations (awards, rankings) [SSZ].
        *   Commentary on responsiveness to price revisions or industry trends [SSX].

### 5. {company_name}'s Competitive Strategy
    *   Describe {company_name}'s stated competitive strategy (e.g., focus on premium segment [SSX], R&D leadership [SSY], operational efficiency [SSZ]). Use direct quotes or paraphrased statements with citations.
    *   Identify and describe {company_name}'s primary value discipline (e.g., operational excellence, customer intimacy, product leadership) if explicitly mentioned, with supporting evidence [SSX].
    *   List specific initiatives or investments by {company_name} aimed at enhancing its competitive position (e.g., "Invested ¥XB in new R&D facility targeting Y technology [SSX]"). Include funding amounts and timelines if available [SSY].
    *   Explain how {company_name} measures its competitive success according to official sources (e.g., target market share growth [SSX], customer satisfaction scores [SSY]).

### 6. General Discussion
    *   Provide a concluding single paragraph (300-500 words) that synthesizes the findings exclusively from Sections 1-5 regarding **{company_name}** and its competitive environment. Clearly link analytical statements using inline citations (e.g., "Given the industry trend towards X [SSY], {company_name}'s investment in Y technology [SSX] positions it well against Competitor A's recent moves [SSZ]..."). Evaluate the overall competitive strength and strategic effectiveness of {company_name}.
    *   Structure the analysis logically by starting with an overall assessment of the competitive landscape and {company_name}'s place within it, discussing strengths/weaknesses/strategy effectiveness in light of competitors and trends, and concluding with strategic implications and potential threats/opportunities from a Japanese perspective.
    *   Do not introduce new factual claims or unsourced analysis.

Source and Accuracy Requirements:
*   **Accuracy**: All information must be factual and current. Specify currency, dates, and reporting periods for any figures. Differentiate between {company_name}'s statements and grounded competitor/industry data. Silently omit unverified data after exhaustive search. Verify table data.
*   **Traceability**: Every claim must include an inline citation ([SSX] for company data, [SSY], [SSZ], etc. for grounded competitor/industry data) corresponding to a grounding URL in the final Sources list.
*   **Source Quality**: Use primarily {company_name}'s official sources. For competitor/industry data, use *only* information verifiable through provided Vertex AI grounding URLs (which might point to reputable third-party sources or competitor reports).

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Management Strategy Prompt
def get_management_strategy_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing management strategy and mid-term business plan with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities.

# Comprehensive Analysis of {company_name}'s Management Strategy and Mid-Term Business Plan: Focus, Execution, and Progress

## Executive Summary

This strategic analysis evaluates **{company_name}**'s management strategy, mid-term business plan execution, and progress against stated objectives. The report examines strategic priorities, resource allocation decisions, performance metrics, and adaptation strategies to assess management effectiveness and strategic direction. Analysis includes detailed review of quantitative targets, operational initiatives, and strategic positioning to provide insights for strategic planning and competitive assessment.

Objective: To conduct an extensive analysis of **{company_name}**'s management strategy and mid-term business plan (MTP) by evaluating strategic pillars, execution effectiveness, progress against targets, and challenges. Focus on explaining *why* strategic choices were made and *how* progress is tracked using specific data with inline citations [SSX]. Focus strictly on {context_str}.

Target Audience Context: This analysis is designed for a **Japanese company** needing deep strategic insights. Present all information with exact dates (e.g., MTP period FY2025-FY2027), reporting periods, financial figures in specified currency, and clear official source attributions [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct in-depth research from official sources for **{company_name}** (IR documents, Annual/Integrated Reports, earnings call transcripts, strategic website sections, MTP presentations). Perform exhaustive checks across multiple sources before silently omitting unverified data. Ensure all claims include inline citations [SSX] and specific dates or reporting periods. Use **perfect Markdown tables** for presenting targets and progress, verifying data accuracy. Use '-' for missing data points only if needed for table structure.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth}
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Strategy Effectiveness Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s strategic direction and execution progress [SSX]
*   **Key Strategic Priorities**: Identify the 3-5 most critical strategic initiatives and their current status [SSY]
*   **MTP Progress Summary**: Summarize progress against mid-term business plan targets and key milestones [SSZ]
*   **Strategic Execution Insights**: Highlight management effectiveness, strategic alignment, and implementation challenges [SSW]
*   **Strategic Recommendations**: List 2-3 priority recommendations for strategic enhancement or course correction [SSV]

## 1. Management Strategy and Vision Alignment:
    *   Outline **{company_name}**'s overall management strategy and analyze its alignment with the company's long-term vision or purpose statement. Include precise references (e.g., "as stated in the Vision 2030 document [SSX]") with inline citations [SSY].
    *   Explain the core management philosophy, values, and strategic approach for {company_name} (e.g., "focus on organic growth through R&D [SSX]", "pursuit of operational excellence [SSY]") with examples, including specific dates or document references [SSZ].
    *   Identify key strategic pillars or themes for {company_name} (e.g., "Digital Transformation", "Sustainability", "Global Expansion") for the upcoming 3-5 years, explaining the rationale and objectives for each based on official statements [SSX, SSY].
    *   Describe any significant strategic shifts from previous plans for {company_name} (e.g., "pivot from hardware to software solutions announced in FY2023 [SSX]"), with supporting data and source references [SSY].

## 2. Current Mid-Term Business Plan (MTP) Overview:
    *   Identify the official name and exact time period of the current MTP for {company_name} (e.g., "Mid-Term Plan 'Growth Forward' (FY2025-FY2027)") with source references [SSX].
    *   Detail the main objectives and specific quantitative targets (financial and non-financial) outlined in the MTP for {company_name}. Present **all** stated MTP targets/KPIs clearly in a **perfectly formatted Markdown table**, including KPI category, KPI name, target value (with currency/units), target year/period, and baseline values if available [SSX]. Verify data accuracy. Use '-' for missing data points only if needed for table structure.
        
        **Example MTP targets table format (replace with actual data)**:
        
        | KPI Category | KPI Name                      | Target Value (by FY2027) | Baseline (FY2024) (if stated) | Source(s) |
        |--------------|------------------------------|--------------------------|-------------------------------|-----------|
        | Financial    | Revenue (JPY Billions)       | 500                      | 350                           | [SS1]     |
        | Financial    | Operating Margin (%)         | 10%                      | 7.5%                          | [SS1]     |
        | Non-Fin      | CO2 Emissions Reduction (%)  | 30%                      | (vs FY2020)                   | [SS2]     |
        | Non-Fin      | Customer Satisfaction Score  | 90                       | -                             | [SS1]     |
    *   Discuss key differences or areas of emphasis compared to the previous MTP for {company_name}, supported by specific examples and inline citations [SSX].

## 3. Strategic Focus Areas and Initiatives within MTP:
    *   For each major strategic pillar identified in the MTP for {company_name}:
        *   Detail the background and specific objectives of that pillar (e.g., "Pillar: Enhance Customer Experience through DX [SSX]"). Explain why it is a priority based on management commentary [SSY].
        *   Describe the relevant market conditions or industry trends cited by the company as influencing this pillar [SSZ].
        *   List specific initiatives, projects, or investments planned under this pillar (e.g., "Launch new CRM platform (Est. Cost: ¥Y Bn) [SSX]", "Invest ¥Z Bn in AI R&D [SSY]"). Include funding details, timelines, and expected outcomes if stated [SSZ].
        *   Assess the potential impact and feasibility of these initiatives based on management commentary or available data [SSX, SSY].

## 4. Execution, Progress Tracking, and Adaptation:
    *   Identify key internal and external challenges or risks acknowledged by {company_name}'s management that affect MTP execution (e.g., "Supply chain disruptions [SSX]", "Talent acquisition difficulties [SSY]").
    *   Describe the specific countermeasures or adjustments stated by {company_name} to address these challenges [SSZ].
    *   Provide the latest available progress updates against the MTP targets for {company_name} (from Section 2 table). Present progress in a **perfectly formatted Markdown table** showing KPI, Target, and Latest Actual/Forecast (with date) [SSX]. Verify data accuracy. Use '-' for missing data points only if needed for table structure.
        
        **Example progress tracking table format (replace with actual data)**:
        
        | KPI Name                      | Target (by FY2027) | Latest Actual/Forecast (as of 2025-03-31) | Progress Notes                                   | Source(s) |
        |-------------------------------|--------------------|--------------------------------------------|--------------------------------------------------|-----------|
        | Revenue (JPY Billions)        | 500                | 410 (FY2025 Forecast)                     | On track / Slightly below forecast              | [SS1]     |
        | Operating Margin (%)          | 10%                | 8.2% (FY2025 Forecast)                    | Facing cost pressures, countermeasures underway  | [SS2]     |
        | CO2 Emissions Reduction (%)   | 30%                | 15% (Achieved 2024)                       | Progressing as planned                           | [SS3]     |
        | Customer Satisfaction Score   | 90                 | -                                          | -                                                |           |
    *   Highlight any significant strategic adjustments or MTP revisions announced by {company_name} in response to performance or external events (e.g., "Revised revenue target downwards in Q2 FY2025 due to market slowdown [SSX]"), with inline citations [SSY].

## 5. General Discussion:
    *   Provide a single concluding paragraph (300-500 words) that synthesizes the key findings from Sections 1-4 regarding **{company_name}**. Clearly connect each analytical insight with inline citations (e.g., "The strategic focus on DX [SSX] aligns with the MTP targets [SSY], although execution progress shows challenges in margin improvement [SSZ]..."). Explain *why* progress is as reported, based on the analysis. Incorporate key quantitative points.
    *   Structure the discussion logically by starting with an overall assessment of the strategy and MTP ambition, discussing execution effectiveness and progress against targets, highlighting key challenges and adaptations, and concluding with strategic takeaways and outlook relevant for a Japanese audience.
    *   Do not introduce any new claims that are not derived from the previous sections and citations about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: Information must be factually correct and current for **{company_name}**. Specify currency and exact dates/periods for all data, targets, and progress reports. Silently omit unverified data after exhaustive search. Verify table data meticulously. Ensure all stated MTP KPIs are captured.
*   **Traceability**: Every claim (in text, tables) must have an inline citation [SSX] linked to the final Sources list.
*   **Source Quality**: Use primarily official company sources for **{company_name}** (MTP documents, IR presentations, Annual Reports, financial results briefings) with clear and verifiable references.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Regulatory Prompt
def get_regulatory_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing the regulatory environment with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f'''

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities.



# In-Depth Analysis of the Regulatory Environment for {company_name}

## Executive Summary

This regulatory analysis examines the legal and compliance framework affecting **{company_name}**'s operations, including applicable regulations, supervisory oversight, licensing requirements, and emerging regulatory trends. The report provides comprehensive insights into regulatory risks, compliance requirements, and strategic implications to support risk management and strategic planning decisions.

**Objective**: To analyze the regulatory environment impacting **{company_name}**, including key laws, licensing, supervisory bodies, market impacts, international comparisons, and recent trends, particularly as they relate to its core business and digital activities. Evaluate the company's stated compliance approaches and any enforcement actions with precise dates and references [SSX]. Focus strictly on {context_str}.

Target Audience Context: The output is for a **Japanese company** reviewing regulatory risks for potential partnership, investment, or competitive evaluation. Provide exact law/regulation names, dates, reporting periods, and detailed official source references [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct deep research on **{company_name}**'s regulatory environment using official documents (e.g., sustainability reports, governance sections, risk factor disclosures in Annual Reports/Filings) and reputable publications (government sites, regulatory body websites, legal updates if grounded). Perform exhaustive checks across multiple sources before silently omitting unverified data. Each claim must be supported by an inline citation [SSX] with specific dates or reporting periods. Use **perfect Markdown formatting**.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on official statements and grounded regulatory info
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Regulatory Environment Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s regulatory landscape and compliance position [SSX]
*   **Key Regulatory Risks**: Identify the 3-5 most significant regulatory challenges, requirements, or emerging changes [SSY]
*   **Compliance Status Summary**: Summarize current compliance posture, regulatory relationships, and any enforcement actions [SSZ]
*   **Regulatory Strategic Insights**: Highlight regulatory implications for business strategy and operational decisions [SSW]
*   **Regulatory Priorities**: List 2-3 priority areas for regulatory attention or risk mitigation [SSV]

### 1. Key Laws, Regulations, and Systems:
    *   **Major Applicable Laws/Regulations**: Identify major laws, ordinances, and ministerial regulations related to **{company_name}**'s industry ('{industry or "N/A"}') and operations (e.g., Pharmaceuticals and Medical Devices Act, Building Standards Act, Telecommunications Business Act, Financial Instruments and Exchange Act, sector-specific environmental laws) [SSX]. Specify jurisdiction (e.g., Japan, EU).
    *   **Government/Agency Guidelines & Standards**: Mention key relevant guidelines or standards issued by government bodies or agencies (e.g., METI's Green Growth Strategy Guidelines, specific cybersecurity frameworks referenced) applicable to {company_name} [SSY].
    *   **Potential Legal Amendments**: Discuss any significant upcoming or recent legal amendments mentioned by {company_name} or in grounded sources that could affect its operations (immediate to long term) [SSZ].

### 2. Licensing and Registration Systems:
    *   **Industry-Specific Permits/Licenses**: Detail any necessary industry-specific permits, licenses, notifications, or registrations required for **{company_name}**'s core business (e.g., manufacturing licenses, financial services licenses, broadcast licenses) [SSX].
    *   **Acquisition & Renewal**: Comment on the perceived difficulty or cost of obtaining/maintaining these licenses for {company_name}, and any recent changes in renewal frequency or examination criteria, if discussed in sources [SSY].

### 3. Supervisory Authorities and Industry Influence:
    *   **Supervisory Bodies**: Identify the main government bodies that supervise **{company_name}**'s industry or key activities (e.g., Financial Services Agency, Ministry of Health Labour and Welfare, Ministry of Internal Affairs and Communications, environmental agencies) [SSX].
    *   **Industry Associations**: Name key industry associations {company_name} is part of that issue regulations, policies, or exert lobbying influence [SSY]. Discuss the influence of these associations on {company_name} if commented upon in sources [SSZ].

### 4. Market and Business Model Impact:
    *   **Competitive Environment Impact**:
        *   Analyze if regulations act as a barrier to new entrants in **{company_name}**'s market [SSX].
        *   Discuss any changes in competitive structure due to deregulation or stricter enforcement mentioned in sources affecting {company_name} [SSY].
        *   Note any competitive advantages derived by {company_name} from legislation (e.g., eligibility for specific subsidies or contracts) [SSZ].
    *   **Business Model Impact**:
        *   Detail key regulatory obligations for {company_name} (e.g., information disclosure, audit compliance, reporting requirements like ESG disclosures) [SSX].
        *   Identify regulatory restrictions impacting {company_name}'s business model (e.g., price controls, advertising restrictions, data usage limitations) [SSY].
        *   Discuss the costs and risks associated with compliance for {company_name} [SSZ].

### 5. International Context (if applicable):
    *   **Comparison for Overseas Expansion**: If **{company_name}** operates internationally or plans expansion, highlight key differences in regulations compared to major overseas markets (e.g., EU regulations, US laws relevant to the industry) based on source information related to {company_name} [SSX].
    *   **International Standards & Certifications**: Note {company_name}'s compliance status with international standards or certifications relevant to regulation (e.g., ISO standards, GDPR compliance statements, CE Mark for products) [SSY].
    *   **Trade Regulations**: Mention regulations or customs clearance systems related to imports and exports relevant to {company_name}'s business, if discussed [SSZ].

### 6. Recent Policy Trends & Developments:
    *   **Latest Trends**: Summarize the latest trends in relevant policies, laws, and regulations mentioned by {company_name} or in grounded sources impacting it [SSX].
    *   **Specific Government Measures**: Detail relevant government initiatives like green policies (subsidies, carbon pricing), DX-related legislation, or support programs impacting {company_name} [SSY].
    *   **ESG-Related Mandates**: Discuss mandatory ESG reporting requirements (e.g., climate change compliance like TCFD, human capital disclosure) applicable to {company_name} [SSZ].
    *   **Social Pressure & Activism**: Mention any significant impact from social pressure or citizen/environmental group activism pushing for stricter regulations or specific corporate actions related to {company_name}, if documented [SSX].

### 7. Compliance Approach & History:
    *   Detail **{company_name}**'s stated compliance approach and governance structure for regulatory matters (e.g., existence of compliance committees, specific policies, training programs) [SSX].
    *   Identify any significant publicly reported regulatory enforcement actions, fines, or controversies related to **{company_name}**'s operations (not just digital) in the last 3-5 years. Specify dates, regulatory bodies involved, outcomes (including fine amounts with currency), and company responses or remedial actions taken [SSY, SSZ]. Present clearly.

## 8. General Discussion:
    *   Provide a concluding single paragraph (300-500 words) that synthesizes the findings from Sections 1-7 regarding **{company_name}**. Clearly articulate the primary regulatory pressures {company_name} faces and assess its apparent compliance posture and risk management effectiveness, using inline citations [SSX, SSY].
    *   Structure the analysis by summarizing the key regulatory domains (general, industry-specific, international, emerging trends), evaluating the company's stated compliance strengths and any reported weaknesses or incidents, and concluding with an overall evaluation of regulatory risk tailored to a Japanese audience (considering factors like operational impact, reputational risk, potential fines, impact on strategy).
    *   Do not introduce new factual claims beyond the provided analysis and citations about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: All regulatory details must be current and verifiable for **{company_name}**. Include specific law names, dates, certification details, and currency information for fines. Silently omit unverified data after exhaustive search.
*   **Traceability**: Each statement must have an inline citation [SSX] corresponding to the final Sources list.
*   **Source Quality**: Use official company disclosures for **{company_name}** (Annual Reports, Sustainability/ESG Reports, Governance sections, specific policy documents if available), government regulatory websites, and reputable news sources only if grounded by Vertex AI Search results.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
'''
    return prompt

# Crisis Prompt
def get_crisis_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing digital crisis management and business continuity with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f'''

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities.

# In-Depth Analysis of {company_name}'s Digital Crisis Management and Business Continuity

## Executive Summary

This crisis management analysis evaluates **{company_name}**'s preparedness for digital threats, business continuity capabilities, and organizational resilience frameworks. The report examines IT security posture, risk management systems, incident response capabilities, and business continuity planning to assess the company's ability to maintain operations during disruptions and recover from potential crises.

Objective: To analyze how **{company_name}** prepares for, manages, and responds to digital crises (e.g., cyberattacks, system outages, data breaches) and its business continuity plans (BCP) related to digital operations. Include details on past incidents with exact dates, impacts (including financial figures with specified currency if reported), company responses, and potential DX-based mitigation strategies linked to identified risks. Use inline citations [SSX]. Focus strictly on {context_str}.

Target Audience Context: This output is for a **Japanese company** assessing digital risk resilience for strategic decision-making. Provide precise data (with dates and reporting periods) and official source references [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct thorough research on **{company_name}**'s crisis management and business continuity from official disclosures (e.g., Annual Reports, Security sections, specific incident reports if published) and reputable reports (cybersecurity news, regulatory filings if grounded). Perform exhaustive checks across multiple sources before silently omitting unverified data. Include inline citations [SSX] for every fact, with specific dates or periods. Use **perfect Markdown formatting**.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on official statements + grounded incident reports
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Crisis Resilience Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s digital crisis preparedness and business continuity capabilities [SSX]
*   **Key Vulnerabilities & Strengths**: Identify the 3-5 most significant crisis management strengths and potential vulnerability areas [SSY]
*   **Incident History Summary**: Summarize notable past incidents, response effectiveness, and lessons learned [SSZ]
*   **Business Continuity Insights**: Highlight crisis management maturity, preparedness gaps, and resilience factors [SSW]
*   **Risk Mitigation Priorities**: List 2-3 priority recommendations for enhancing crisis preparedness and response capabilities [SSV]

## 1. Crisis Management and Business Continuity:
    *   **Handling of Past Digital Crises (Last 5 Years)**: Describe significant publicly reported digital crises impacting **{company_name}**. Use bullet points for each incident:
        *   **Incident Type & Date**: (e.g., Ransomware attack, approx. 2024-08 [SSX]; Major system outage, 2024-03-15 [SSY]; Data breach discovered 2023-11 [SSZ]).
        *   **Impact Details**: Describe affected systems/services, nature of data compromised (if applicable), estimated number of users/customers affected, duration of outage, and any reported financial impact (e.g., estimated recovery costs of $X million [SSX], fine of €Y million [SSY]). Be specific and cite sources.
        *   **Company Response**: Detail **{company_name}**'s public statements, communication strategy, remedial actions taken (e.g., systems restored by [Date] [SSX], external cybersecurity experts engaged [SSY], free credit monitoring offered [SSZ]), and any reported changes to security practices or governance resulting from the incident [SSW].
        *   **Lessons Learned (if stated)**: Include any officially stated lessons learned or future preventative measures mentioned by **{company_name}** [SSX].
    *   **Stated Preparedness and Planning**:
        *   Explain **{company_name}**'s stated approach to digital crisis management. Mention existence of an Incident Response Plan (IRP), Cyber Incident Response Team (CIRT), or similar structures if documented [SSX].
        *   Describe **{company_name}**'s stated approach to Business Continuity Planning (BCP) specifically for digital operations. Mention existence of BCP documents, disaster recovery (DR) sites, recovery time objectives (RTOs) or recovery point objectives (RPOs) if disclosed [SSY].
        *   Outline the governance structure within **{company_name}** involved in overseeing digital risk, crisis management, and BCP (e.g., Board committee oversight [SSX], role of CISO/CIO [SSY]). Cite specific sources.
        *   Mention any regular drills, simulations, or third-party audits related to crisis response or BCP conducted by **{company_name}**, if disclosed [SSZ].
    *   **Risk Forecasting & DX Mitigation (Analysis)**:
        *   Discuss any forward-looking risk assessments or forecasting of potential future crisis impacts mentioned in **{company_name}**'s reports (e.g., risk factors section: natural disasters affecting data centers, major supply chain digital disruptions) [SSX].
        *   Based on the identified risks for {company_name} [SSX] or past incident types [SSY], analyze and propose relevant Digital Transformation (DX) based solutions or mitigation strategies that could enhance its resilience (e.g., "Given {company_name}'s stated risk of seismic activity near HQ [SSX], DX solutions like geographically distributed cloud backups and enhanced remote work capabilities could mitigate operational disruption."). *This analysis should logically connect identified risks to known DX capabilities.*

## 2. General Discussion:
    *   Provide a concluding single paragraph (300-500 words) synthesizing the findings from Section 1 regarding **{company_name}**. Assess its apparent resilience to digital disruptions based on its history of incidents, responses, stated preparedness, and the potential application of DX for mitigation. Use inline citations explicitly (e.g., "The company's response to the 2024 incident [SSX] suggests an established protocol, though the stated RTO [SSY] raises questions... The identified risk of X [SSZ] could potentially be addressed by DX initiatives focused on Y...").
    *   Structure the discussion logically, starting with a summary of the incident history and response effectiveness, followed by an evaluation of the stated preparedness measures (IRP, BCP) and risk awareness, incorporating the potential role of DX, and concluding with an assessment of overall digital resilience for {company_name}, identifying potential strengths and weaknesses relevant to a Japanese audience considering partnership or investment.
    *   Do not introduce any new claims not supported by the previous analysis and citations about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: All incident details, dates, financial impacts (with currency), and response measures must be current and verifiable against grounded sources for **{company_name}**. Silently omit unverified data after exhaustive search. Proposed DX solutions should be logical extensions of identified risks/tech capabilities.
*   **Traceability**: Every factual claim must include an inline citation [SSX] linked to a source in the final Sources list.
*   **Source Quality**: Prioritize official company disclosures for **{company_name}** (press releases on incidents, security sections in reports). Use reputable news or cybersecurity firm reports *only* if grounded by Vertex AI Search results.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
'''
    return prompt

# Digital Transformation Prompt
def get_digital_transformation_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing DX strategy and execution with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities.

# In-Depth Analysis of {company_name}'s Digital Transformation (DX) Strategy and Execution

## Executive Summary

This digital transformation analysis examines **{company_name}**'s DX strategy, implementation progress, and investment priorities across technology modernization, process automation, and digital capability building. The report evaluates strategic vision, resource allocation, execution effectiveness, and business impact to assess digital maturity and competitive positioning in the digital economy.

Objective: To analyze **{company_name}**'s Digital Transformation (DX) strategy, including its vision, the rationale behind it, key priorities, major investments, and specific case studies of digital initiatives. Evaluate also how DX integrates compliance and crisis management considerations. Use precise data (e.g., specific investment amounts with currency, dates) supported by inline citations [SSX]. Focus strictly on {context_str}.

Target Audience Context: The analysis is prepared for a **Japanese company** assessing {company_name}'s digital maturity and strategy. Therefore, it must be detailed, with exact figures (specifying currency and reporting periods) and official source references [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct detailed research on **{company_name}**'s DX journey using official sources (company reports, dedicated DX sections on website, investor presentations, press releases) and reputable analyses (if grounded). Perform exhaustive checks across multiple sources before silently omitting unverified data. Every claim, financial figure, and example must include an inline citation [SSX] and specific dates or periods. Use **perfect Markdown formatting**. Use '-' for missing data points in tables only if needed for structure. Verify data accuracy.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on DX strategy documents, IR materials
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Digital Transformation Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s DX strategy, progress, and digital maturity [SSX]
*   **Key DX Initiatives**: Identify the 3-5 most significant digital transformation priorities and their implementation status [SSY]
*   **Investment & ROI Summary**: Summarize DX investments, resource allocation, and measurable business impact [SSZ]
*   **Digital Capability Insights**: Highlight digital strengths, gaps, and strategic positioning in the digital economy [SSW]
*   **DX Strategic Recommendations**: List 2-3 priority recommendations for accelerating digital transformation success [SSV]

## 1. DX Strategy Overview:
    *   Outline **{company_name}**'s overall digital transformation vision and strategic goals (e.g., "To become a data-driven organization by 2030 [SSX]", "Enhance customer experience through personalized digital services [SSY]"). Use verbatim statements where possible, with precise references and inline citations [SSZ].
    *   **Analyze the Rationale**: Based on management commentary or strategic documents for {company_name}, explain the *reasons* behind its DX strategy (e.g., "What business problems is DX aiming to solve? How does it link to competitive pressures or the overall corporate vision?") [SSX, SSY].
    *   Identify the key strategic priorities or pillars of {company_name}'s DX strategy (e.g., "Cloud Migration", "AI & Analytics adoption", "Workforce Digital Upskilling", "Supply Chain Optimization") with specific details and start/end dates if part of a formal plan [SSX].
    *   List major DX initiatives or projects for {company_name} currently underway or recently completed under these pillars. Include specific objectives and target outcomes for each initiative if stated (e.g., "Project Phoenix: Cloud migration targeting X% cost reduction by 2026 (FY2025) [SSX]", "Invest ¥Z Bn in AI R&D [SSY]"). Include funding details, timelines, and expected outcomes if stated [SSZ].

## 2. DX Investments Analysis (Last 3 Fiscal Years):
    *   Analyze **{company_name}**'s investments specifically allocated to DX, if disclosed. Provide detailed breakdowns by initiative or area (e.g., cloud infrastructure, AI development, cybersecurity enhancements related to DX) if available, potentially in a **perfectly formatted Markdown table**. Include specific investment amounts (with currency), funding sources (if mentioned), timelines, and reporting periods, with inline citations [SSX]. Verify data accuracy. Use '-' for missing data points only if needed for table structure.
        | DX Investment Area        | FY2023 (JPY M) | FY2024 (JPY M) | FY2025 (JPY M) | Notes / Key Projects        | Source(s) |
        |---------------------------|----------------|----------------|----------------|---------------------------|-----------|
        | Cloud Migration           | 10,000         | 12,500         | 15,000         | e.g., AWS/Azure spend     | [SS1]     |
        | AI & Data Analytics       | 5,000          | 7,000          | 9,000          | e.g., Platform build      | [SS2]     |
        | Process Automation (RPA)  | 2,000          | 3,000          | 4,000          | RPA implementations       | [SS3]     |
        | Customer Facing Platforms | 8,000          | 10,000         | 11,000         | e.g., New CRM/App dev     | [SS4]     |
        | Total DX Spend (if stated)| 25,000         | 32,500         | 39,000         |                           | [SS5]     |
    *   Describe overall investment trends in DX for {company_name} over the last 3 years (e.g., increasing significantly [SSX], stable focus on specific areas [SSY]) with supporting data and analysis of the investment allocation strategy [SSZ].

## 3. DX Case Studies & Implementation Examples:
    *   Provide detailed descriptions of 2-3 specific DX implementation examples or case studies highlighted by **{company_name}**. For each example, describe:
        *   **Initiative Name & Goal**: (e.g., "Smart Factory Project [SSX]", "Goal: Improve OEE by 15%")
        *   **Technology Involved**: (e.g., IoT sensors, predictive analytics platform, cloud data lake) [SSY]
        *   **Implementation Details**: (e.g., Phased rollout across 3 plants starting 2023 [SSX], Partnership with Vendor V [SSZ])
        *   **Measurable Outcomes & Business Impact**: Quantify results where possible (e.g., "Achieved 12% improvement in OEE in Plant A [SSX]", "Reduced manual reporting time by X hours/week [SSY]", "Enabled new service generating ¥Z million in first year [SSZ]"). Specify currency and reporting period. Use only company-reported outcomes for {company_name}.
        *   **Rationale for Highlighting**: Explain why this example was likely chosen by {company_name} (e.g., flagship project demonstrating AI capability [SSX], successful cross-functional collaboration [SSY]).

## 4. Regulatory Environment, Compliance, and Crisis Management (Integration with DX):
    *   Briefly summarize the key regulatory trends previously identified (in the Regulatory prompt context, if available) that directly impact **{company_name}**'s DX strategy (e.g., data localization requirements affecting cloud choices [SSX], security standards for connected devices [SSY]). Cite specific laws or standards and sources.
    *   Describe how **{company_name}** states it integrates compliance considerations into its DX efforts (e.g., "Privacy by Design principles applied in new app development [SSX]", "Mandatory security reviews for all new cloud services [SSY]"). Provide specific examples from official sources [SSZ].
    *   Mention how digital crisis management and business continuity considerations are addressed within the context of major DX initiatives at **{company_name}** (e.g., "Disaster recovery plans tested for new cloud platform [SSX]", "Redundancy built into critical digital infrastructure [SSY]"). Cite official examples where available [SSZ].

## 5. General Discussion:
    *   Provide a concluding single paragraph (300-500 words) that synthesizes the findings from Sections 1-4 regarding **{company_name}**. Assess the coherence, ambition, rationale, and execution progress of {company_name}'s DX strategy. Explicitly link data points and examples using inline citations (e.g., "The strategic rationale focusing on customer experience [SSX] drives the significant investment in CRM [SSY], and early results from case studies [SSZ] suggest potential, though scaling remains a challenge...").
    *   Structure your discussion logically—start with an overview of the DX strategy's clarity and focus, evaluate the investment commitment and implementation effectiveness based on examples, integrate the handling of compliance and risk, and conclude with an assessment of the DX maturity and outlook relevant for a Japanese audience.
    *   Do not introduce new facts outside of the presented analysis and citations about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: All data must be current and verified for **{company_name}**. Specify currency and reporting period for every monetary value, investment figure, and outcome metric. Silently omit unverified data after exhaustive search. Verify table data meticulously.
*   **Traceability**: Every fact must include an inline citation [SSX] that corresponds to a source in the final Sources list.
*   **Source Quality**: Prioritize official company disclosures for **{company_name}** (Annual Reports, IR presentations, specific DX reports/webpages) and reputable research *only if grounded* by Vertex AI Search results.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Business Structure Prompt
def get_business_structure_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing business structure, geographic footprint, ownership, and leadership linkages with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    business_structure_completion_guidance = textwrap.dedent(f"""\
    **Critical Data Focus for Business Structure**:

    *   **Priority Information**: Strive to provide, based on exhaustive search of verifiable sources for **{company_name}**:
        1. The business segment breakdown table using the company's reported segmentation and metrics (e.g., revenue, premiums in-force), with at least the most recent fiscal year data (% and absolute value) [SSX].
        2. The geographic segment breakdown table using the company's reported segmentation and metrics, with at least the most recent fiscal year data (% and absolute value) [SSX].
        3. The top 3-5 major shareholders table with percentages and as-of dates [SSX].

    *   **Check for Alternative Metrics**: If standard revenue segmentation is not the primary method used by {company_name} (e.g., in MTP targets, core reporting for industries like insurance), look for and report the segmentation based on the key metric the company uses (e.g., premiums in-force, assets under management). Clearly define the metric used based on the source.
    *   **Partial Data Handling**: If only partial data (e.g., 1-2 years instead of 3) is available for segments/geography after exhaustive search for {company_name}, present the available data clearly in the tables, noting the timeframe covered (e.g., in the text analyzing the table: "Data for FY2023-2024 shows..." [SSX]). Do not state unavailability. Proceed with analysis based on the available timeframe.

    *   **Verification**: Before completing each section, internally verify:
        * All priority information points are addressed using available grounded data for {company_name}.
        * At least one full fiscal year of data is provided for segments and geography tables if verifiable, using the correct metric/segmentation.
        * All available verified ownership information is included in the table.
        * Each data point includes proper inline citation [SSX] and data verified against source.
    """)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities.

# In-Depth Analysis of {company_name}'s Business Structure, Geographic Footprint, Ownership, and Strategic Vision Linkages

## Executive Summary

This structural analysis examines **{company_name}**'s business segmentation, geographic presence, ownership composition, and organizational design. The report provides detailed insights into revenue distribution by business unit and geography, shareholder structure, operational footprint, and strategic alignment to support investment decisions and partnership evaluations.

Objective: To analytically review **{company_name}**'s operational structure (by business and geography, using company-reported metrics), ownership composition, and how these elements link to leadership's stated strategic vision. Include specific figures (with currency and fiscal year), and reference official sources (e.g., Annual Report, IR materials, Filings) with inline citations [SSX]. Focus strictly on {context_str}.

Target Audience Context: This output is intended for a **Japanese company** performing market analysis and partnership evaluation. Present all claims with exact dates, detailed quantitative figures, and clear source references [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Perform a critical analysis using official sources for **{company_name}** (Annual/Integrated Reports, IR materials, filings like Yukashoken Hokokusho, corporate governance documents). Supplement with reputable secondary sources only when necessary and grounded. Perform exhaustive checks across multiple sources before silently omitting unverified data. Ensure each claim includes an inline citation [SSX] and precise data (e.g., "as of YYYY-MM-DD"). Use **perfect Markdown tables**. Verify data accuracy. Use '-' for missing data points only if needed for table structure. Look for the primary segmentation metric used by the company (e.g., revenue, premiums in-force).
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth}
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}
{business_structure_completion_guidance}

{formatted_additional_instructions}

## Executive Summary
*   **Business Structure Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s business structure, geographic footprint, and organizational design [SSX]
*   **Key Structural Insights**: Identify the 3-5 most significant structural characteristics, segment performance, and geographic strengths [SSY]
*   **Ownership & Control Summary**: Summarize ownership structure, governance implications, and stakeholder influence [SSZ]
*   **Strategic Alignment Insights**: Highlight how business structure supports strategic vision and operational effectiveness [SSW]
*   **Structural Optimization Recommendations**: List 2-3 priority recommendations for structural or operational enhancement [SSV]

## 1. Business Segment Analysis (Last 3 Fiscal Years):
    *   List the reported business segments for **{company_name}** using official descriptions. Identify the primary metric used for segmentation (e.g., Revenue, Premiums In-Force). Include a **perfectly formatted Markdown table** with consolidated figures for that metric (specify metric, currency, and fiscal year) and composition ratios (%), with each data point referenced [SSX]. Ensure totals sum correctly if verifiable. Verify data accuracy. Use '-' for missing data points only if needed for table structure.
        
        **Example business segment table format (replace with actual data)**:
        
        | Segment Name | FY2023 Metric Value (Unit) | FY2023 (%) | FY2024 Metric Value (Unit) | FY2024 (%) | FY2025 Metric Value (Unit) | FY2025 (%) | Source(s) |
        |--------------|--------------------------|------------|--------------------------|------------|--------------------------|------------|-----------|
        | Segment A    | 100,000                  | 40%        | 110,000                  | 41%        | 120,000                  | 42%        | [SS1]     |
        | Segment B    | 80,000                   | 32%        | 85,000                   | 32%        | 90,000                   | 32%        | [SS2]     |
        | Segment C    | 70,000                   | 28%        | 72,000                   | 27%        | 75,000                   | 26%        | [SS3]     |
        | Adjustments  | 0                        | 0%         | 0                        | 0%         | 0                        | 0%         | [SS4]     |
        | **Total**    | 250,000                  | **100%**   | 267,000                  | **100%**   | 285,000                  | **100%**   | [SS5]     |
    *   For each major segment of {company_name}, briefly describe its products/services [SSX] and analyze significant trends (e.g., growth/decline rates YoY calculated from table data, changes in contribution ratio) with specific percentages and dates [SSY]. Identify the fastest growing and/or most profitable segments based on available data (growth in the reported metric, operating income/margin if reported per segment in source documents) [SSZ].

## 2. Geographic Segment Analysis (Last 3 Fiscal Years):
    *   List the geographic regions or segments as reported by **{company_name}** (e.g., Japan, North America, Europe, Asia). Identify the primary metric used for geographic segmentation. Include a **perfectly formatted Markdown table** with corresponding figures (specify metric, currency, fiscal year) and composition ratios (%), ensuring totals sum correctly if verifiable [SSX]. Verify data accuracy. Use '-' for missing data points only if needed for table structure.
        
        **Example geographic segment table format (replace with actual data)**:
        
        | Geographic Region | FY2023 Metric Value (Unit) | FY2023 (%) | FY2024 Metric Value (Unit) | FY2024 (%) | FY2025 Metric Value (Unit) | FY2025 (%) | Source(s) |
        |-------------------|--------------------------|------------|--------------------------|------------|--------------------------|------------|-----------|
        | Japan             | 100,000                  | 40%        | 105,000                  | 39%        | 110,000                  | 39%        | [SS1]     |
        | North America     | 75,000                   | 30%        | 81,000                   | 30%        | 88,000                   | 31%        | [SS2]     |
        | Europe            | 50,000                   | 20%        | 54,000                   | 20%        | 57,000                   | 20%        | [SS3]     |
        | Asia (ex-Japan)   | 25,000                   | 10%        | 27,000                   | 10%        | 30,000                   | 10%        | [SS4]     |
        | Other             | 0                        | 0%         | 0                        | 0%         | 0                        | 0%         | [SS5]     |
        | **Total**         | 250,000                  | **100%**   | 267,000                  | **100%**   | 285,000                  | **100%**   | [SS6]     |
    *   Analyze regional trends for {company_name} (growth/decline YoY calculated from table data, changes in contribution) with specific supporting data [SSX]. Identify key growth markets and declining markets with specific figures [SSY]. Note any stated plans for geographic expansion or contraction with dates and details mentioned in reports [SSZ].

## 3. Major Shareholders & Ownership Structure:
    *   Describe the overall ownership type for **{company_name}** (e.g., publicly traded on TSE Prime [SSX], privately held) with specific details [SSY].
    *   List the top 5-10 major shareholders of {company_name} in a **perfectly formatted Markdown table** with exact names (as reported, e.g., trust banks), precise ownership percentages, shareholder type (institutional, individual, government, etc.), and the 'as of' date for the data [SSX]. Note any significant changes in top holders over the past year if reported [SSY]. Verify data. Use '-' for missing data points only if needed for table structure.
        
        **Example shareholders table format (replace with actual data)**:
        
        | Shareholder Name          | Ownership % | Shareholder Type     | As of Date   | Source(s) |
        |---------------------------|-------------|----------------------|--------------|-----------|
        | The Master Trust Bank of Japan, Ltd. | 9.8%        | Institutional (Trust)| 2024-03-31   | [SS1]     |
        | Custody Bank of Japan, Ltd.| 7.5%        | Institutional (Trust)| 2024-03-31   | [SS1]     |
        | [Founder's Name]          | 5.2%        | Individual (Founder) | 2024-03-31   | [SS2]     |
        | JP Morgan Chase Bank, N.A.| 4.1%        | Institutional        | 2024-03-31   | [SS3]     |
        | Nomura Securities Co., Ltd.| 3.8%        | Institutional        | 2024-03-31   | [SS4]     |
        
        **NOTE: These shareholder names and details are examples only. Replace with actual verified shareholders of {company_name}.**
    *   Include key figures for {company_name} like Total Shares Outstanding [SSX], Treasury Stock [SSY], and Free Float percentage (if available) [SSZ], all with 'as of' dates. Mention controlling shareholders or parent company relationships if applicable [SSX]. Discuss any known cross-shareholdings with major business partners if material and reported [SSY].
    *   Comment briefly on ownership concentration for {company_name} and potential implications (e.g., high institutional ownership suggests focus on governance [SSX], stable founder ownership may influence long-term strategy [SSY]).

## 4. Corporate Group Structure:
    *   Describe the parent-subsidiary relationships and overall corporate group structure for **{company_name}** based on official filings or reports (e.g., list of major subsidiaries in Annual Report Appendix [SSX]). Note existence/location of group structure charts if found [SSY].
    *   List key operating subsidiaries of {company_name} in a **perfectly formatted Markdown table**, including their official names, primary business functions/segments they operate in, country/region of incorporation, and ownership percentage by the parent company (if stated) [SSX]. Verify data. Use '-' for missing data points only if needed for table structure.
        
        **Example subsidiaries table format (replace with actual data)**:
        
        | Subsidiary Name             | Primary Business Function / Segment | Country/Region | Ownership % | Source(s) |
        |-----------------------------|-------------------------------------|----------------|-------------|-----------|
        | {company_name} USA Inc.     | Sales & Marketing (Cloud Services)  | USA            | 100%        | [SS1]     |
        | {company_name} Europe GmbH  | R&D, Manufacturing (AI Solutions)   | Germany        | -           | [SS2]     |
        | Joint Venture Alpha Co., Ltd. | Specific Technology Development     | Japan          | 50%         | [SS3]     |
        | {company_name} Asia Pte. Ltd.| Regional Operations (Cybersecurity) | Singapore      | 100%        | [SS4]     |
        
        **NOTE: These subsidiary examples are purely fictional. Replace with actual verified subsidiaries of {company_name} from official sources.**

## 5. Leadership Strategic Outlook & Vision (Verbatim Quotes - Linkages):
    *   Provide verbatim quotes from key executives of **{company_name}** (CEO, Chairman, and optionally CFO/CSO) that specifically address:
        * Long-term strategic vision related to business segments or geographic focus [SSX].
        * Plans for specific business segment growth/rationalization or geographic expansion [SSY].
        * Comments linking the corporate structure (including subsidiaries or group reorganization) to strategy execution [SSZ].
        * Comments on ownership structure or major shareholder relations (if any and if public) [SSW].
    *   Each quote must have its source cited immediately after it (e.g., "(Source: Integrated Report 2025, p. 5)") and an inline citation [SSX] confirming the quote's origin.
    *   Where possible, explicitly connect a quote to a specific finding in Sections 1-4 (e.g., "Reflecting the growth in the Asian market shown in Section 2 [SSY], the CEO stated, '...' [SSX]").

## 6. General Discussion:
    *   Provide a single concluding paragraph (300-500 words) that synthesizes the findings from Sections 1-5 regarding **{company_name}**. Clearly link analytical insights and comparisons using inline citations (e.g., "The shift in segment focus towards Segment B [SSX] aligns with the CEO's stated focus [SSY], but geographic concentration in Japan [SSZ] remains a key factor influencing growth prospects..."). Incorporate key quantitative points.
    *   Address specifically:
        * The alignment (or misalignment) between the business/geographic structure (using the relevant metric) and the stated strategic vision/MTP for {company_name} [SSX, SSY].
        * How the ownership structure may influence business decisions or governance at {company_name} [SSZ].
        * Key opportunities or challenges presented by {company_name}'s current segment mix and geographic footprint [SSW].
        * Potential future developments or necessary structural changes based on {company_name}'s current structure, trends, and leadership comments [SSX, SSY].
    *   Structure your discussion logically, starting with a summary of business and geographic drivers, assessing ownership influence and leadership vision alignment, and concluding with strategic implications for a Japanese audience.
    *   Do not introduce new unsupported claims about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: Ensure all data is precise for **{company_name}**, with currency and fiscal year reported for numerical values. Use official names for segments, regions, shareholders, and subsidiaries. Use the correct segmentation metric as reported by the company. Silently omit unverified data after exhaustive search. Verify table data meticulously.
*   **Traceability**: Every fact (in text, tables) must include an inline citation [SSX] corresponding to the final Sources list.
*   **Source Quality**: Use only primary official sources for **{company_name}** (Annual/Integrated Reports, Financial Statements, Filings, IR Presentations, Governance Reports) with clear documentation references.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Vision Prompt
def get_vision_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing corporate vision and purpose with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities.



# Analysis of {company_name}'s Strategic Vision and Purpose

## Executive Summary

This strategic vision analysis examines **{company_name}**'s stated mission, vision, and corporate purpose, evaluating strategic themes, implementation approach, and progress measurement systems. The report provides comprehensive insights into organizational direction, strategic priorities, and stakeholder commitments to assess strategic clarity and execution capability.

**Objective**: To provide a detailed analysis of **{company_name}**'s officially stated vision, mission, or purpose. Break down its core components (pillars, strategic themes), explain how progress is measured using specific KPIs mentioned in relation to the vision, and assess stakeholder focus. Include exact quotes, dates, and reference all information using inline citations [SSX]. Use the latest available sources. Focus strictly on {context_str}.

Target Audience Context: This analysis is for a **Japanese company** assessing strategic alignment and long-term direction. Present precise information with clear source references and detailed explanations (e.g., "as per the Integrated Report 2025, p.12, [SSX]") {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct in-depth research using official sources for **{company_name}** such as the company website (strategy, about us, IR, sustainability pages), Annual/Integrated Reports, MTP documents, and press releases detailing the corporate vision or purpose. Perform exhaustive checks across multiple sources before silently omitting unverified data. Every claim or data point must have an inline citation [SSX] and include specific dates or document references. Use **perfect Markdown formatting**. Verify data accuracy. Use '-' for missing data points in tables only if needed for structure.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on vision/mission statements, strategic pillars
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **Vision & Purpose Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s strategic vision, mission clarity, and purpose alignment [SSX]
*   **Key Strategic Themes**: Identify the 3-5 most significant strategic pillars and their implementation progress [SSY]
*   **Vision Execution Summary**: Summarize how the vision translates into measurable objectives and operational priorities [SSZ]
*   **Stakeholder Alignment Insights**: Highlight vision clarity, stakeholder commitment, and organizational alignment [SSW]
*   **Vision Enhancement Recommendations**: List 2-3 priority recommendations for strengthening vision execution or strategic clarity [SSV]

## 1. Company Vision and Strategy Elements:
    *   **Vision/Purpose/Mission Statement**: Present **{company_name}**'s official statement(s) verbatim (e.g., "Our Purpose is to...") with an inline citation [SSX] identifying the source document and date (e.g., Integrated Report 2025 [SSX]). Explain its core message and intended timescale (e.g., Vision 2030) [SSY].
    *   **Strategic Vision Components/Pillars**: List and explain the key strategic themes, values, or pillars that underpin the vision for {company_name} (e.g., "Innovation", "Sustainability", "Customer Centricity") as defined in official documents [SSX]. Provide brief definitions or explanations for each pillar based on the source [SSY].
    *   **Vision Measures / KPIs**: Identify specific measures or Key Performance Indicators (KPIs) that **{company_name}** explicitly links to tracking progress towards its overall vision or purpose (these might be high-level MTP targets or specific ESG goals mentioned in the vision context). Present these in a list or **perfectly formatted Markdown table** if multiple and verifiable, including the KPI name, the target (if specified, with date/period), and how it relates to the vision pillar [SSX]. Verify data. Use '-' for missing data points only if needed for table structure.
        
        **Example KPI table format (replace with actual data)**:
        
        | Vision Pillar       | Linked KPI                     | Target/Goal (if specified)      | Source(s) |
        |--------------------|--------------------------------|--------------------------------|-----------|
        | Sustainability      | Scope 1+2 CO2 Reduction        | 50% reduction by 2030 vs 2020  | [SS1]     |
        | Innovation          | % Revenue from New Products    | 20% by FY2027                  | [SS2]     |
        | Customer Centricity | Net Promoter Score (NPS)       | > 50 by 2027                   | [SS3]     |
    *   ***Stakeholder Focus***: Analyze how the vision statement and its supporting pillars for {company_name} explicitly address or prioritize key stakeholder groups (e.g., customers, employees, shareholders, society, environment) based on the language used in official communications [SSX]. Provide specific examples or quotes [SSY].

## 2. General Discussion:
    *   Provide a concluding single paragraph (300-500 words) that synthesizes the information in Section 1 regarding **{company_name}**. Evaluate the clarity, ambition, distinctiveness, and internal coherence of the stated vision and its components. Use inline citations to link back to specific elements (e.g., "The vision's focus on sustainability [SSX] is clearly measured by the CO2 reduction KPI [SSY], demonstrating commitment... However, the link between the 'Innovation' pillar and specific KPIs appears less defined [SSZ] based on available public disclosures..."). Incorporate key quantitative points if available.
    *   Structure the analysis logically—start with an overall summary of the vision's core message, discuss the strength and measurability of its components and stakeholder considerations, and finally evaluate its potential effectiveness in guiding strategy and its relevance for a Japanese audience assessing long-term direction.
    *   Do not introduce new claims beyond the synthesized findings from Section 1 and citations about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: Ensure all statements, quotes, and KPIs for **{company_name}** are accurately represented from official sources and current as of the cited document date. Specify currency/units for KPIs where applicable. Silently omit unverified data after exhaustive search. Verify table data.
*   **Traceability**: Every claim must have an inline citation [SSX] that corresponds to a source in the final Sources list.
*   **Source Quality**: Use primarily official company documents for **{company_name}** (Integrated Reports, dedicated Vision/Purpose web pages, MTP overviews, Sustainability Reports) and well-documented press releases related to strategy announcements.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# Management Message Prompt
def get_management_message_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for collecting strategic quotes from leadership with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company and the speaker for all sourced information. Do not include unrelated entities.

# Detailed Leadership Strategic Outlook (Verbatim Quotes) for {company_name}

## Executive Summary

This leadership communication analysis compiles direct strategic statements from **{company_name}**'s senior management to provide insights into strategic direction, priorities, and organizational vision. The report captures verbatim quotes from key executives to assess management philosophy, strategic focus areas, and leadership alignment on critical business initiatives.

Objective: To compile a collection of direct, verbatim strategic quotes from **{company_name}**'s senior leadership (primarily CEO and Chairman, but also including other key C-suite executives like CFO, CSO, CTO, COO, or relevant BU Heads if their verifiable quotes offer significant strategic insight) that illustrate the company's strategic direction, key priorities, future plans, market outlook, and responses to major challenges. Each quote must be accurately transcribed with an immediate source citation in parentheses and an inline citation [SSX] confirming its origin. Focus strictly on leadership of {context_str}.

Target Audience Context: This information is for a **Japanese company** that requires a clear understanding of leadership's strategic communication and tone. Ensure that every quote includes the speaker's name and title, the exact source document/event, date, and page/timestamp if available [SSX]. {formatted_audience_reminder}

{get_language_instruction(language)}

Research Requirements:
Conduct focused research on recent (last 1-2 years) official communications from **{company_name}**'s leadership (e.g., CEO/Chairman messages in Annual/Integrated Reports, Earnings Call Transcripts Q&A sections, Investor Day presentations, Keynote speeches, official interviews published by reputable sources if grounded). Perform exhaustive checks across multiple sources before silently omitting unverified quotes. Extract strategically relevant verbatim quotes. Each quote must have an inline citation [SSX] and be followed by its specific source reference in parentheses. Use **perfect Markdown formatting**, especially for the quote blocks.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on primary comms: Reports, Transcripts, IR events
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION} # Focus synthesis on themes within quotes

{formatted_additional_instructions}

## Executive Summary
*   **Leadership Communication Assessment**: Provide a concise 250-300 word executive summary of **{company_name}**'s leadership messaging, strategic themes, and management philosophy [SSX]
*   **Key Leadership Priorities**: Identify the 3-5 most significant strategic priorities and themes emerging from leadership communications [SSY]
*   **Management Alignment Summary**: Summarize consistency of messaging across leadership team and strategic coherence [SSZ]
*   **Strategic Direction Insights**: Highlight leadership vision clarity, change management approach, and stakeholder communication effectiveness [SSW]
*   **Leadership Communication Recommendations**: List 2-3 observations about leadership messaging and strategic direction [SSV]

## 1. Leadership Strategic Outlook (Verbatim Quotes):

### [CEO Full Name], [CEO Title] (of {company_name})
- Provide a brief 1-2 sentence summary of the key strategic themes reflected in the CEO's quotes below (e.g., Emphasis on digital transformation and global markets during FY2024 reporting [SSX]). Cite the source range.

**Quote 1 (Theme: e.g., Long-Term Vision)**:
> "..." [SSX]
(Source: [Annual Report 2025], [2025-06-15], [p.10])

**Quote 2 (Theme: e.g., Key Challenge Response)**:
> "..." [SSY]
(Source: [Earnings Call Transcript Q4 FY2024], [2025-05-10], [min 23:45])

**Quote 3 (Theme: e.g., Growth Strategy)**:
> "..." [SSZ]
(Source: [Investor Day Presentation 2025], [2025-09-20], [slide 15])

**Quote 4 (Theme: e.g., Market Outlook)**:
> "..." [SSW]
(Source: [Corporate Website 'CEO Message'], [Accessed 2025-10-01])

*(Add more quotes if particularly insightful and verifiable, aim for 3-5 key strategic quotes)*

### [Chairman Full Name], [Chairman Title] (of {company_name}, if distinct from CEO and provides verifiable strategic commentary)
- Provide a brief 1-2 sentence summary of key themes in the Chairman's quotes (include date range) [SSX].

**Quote 1 (Theme: e.g., Governance/Sustainability)**:
> "..." [SSV]
(Source: [Integrated Report 2025], [2025-07-01], [p.5])

**Quote 2 (Theme: e.g., Long-term Perspective)**:
> "..." [SSU]
(Source: [Annual Shareholders' Meeting Minutes 2025], [2025-06-25])

*(Add more quotes if available, verifiable, and strategically relevant, aim for 2-3)*

### [Other Key Executive Name], [Title] (e.g., CFO, CSO, CTO, COO, BU Head of {company_name} - Include significant, verifiable strategic quotes)
- Provide a brief 1-2 sentence summary of their strategic focus area reflected in verifiable quotes [SSX].

**Quote 1 (Theme: e.g., Financial Strategy / Tech Roadmap / Operational Excellence)**:
> "..." [SST]
(Source: [Document/Event Name], [Date], [Page/Timestamp if available])

*(Include 1-3 highly relevant, verifiable quotes per key executive if applicable)*

## 2. General Discussion:
    *   Provide a concluding single paragraph (300-500 words) that synthesizes the key strategic messages, priorities, and tone conveyed *exclusively* through the collected, verifiable quotes from **{company_name}**'s leadership in Section 1. Identify recurring themes, potential shifts in focus, or areas where different executives provide complementary perspectives. Use inline citations to link back to specific quotes or speakers (e.g., "The CEO's emphasis on digital innovation [SSX, SSZ] aligns with the CTO's focus on AI investment [SST], suggesting a unified direction... However, the Chairman's cautionary note on governance [SSV] highlights potential execution risks..."). Consider potential DX opportunities or challenges implied by the leadership messages [SSX].
    *   Structure your analysis logically: summarize the dominant strategic narrative from leadership based on the quotes, highlight any nuances or potential tensions between messages, and conclude with an assessment of the clarity and consistency of the strategic communication relevant for a Japanese audience interpreting leadership signals.
    *   Do not introduce any new factual claims or analysis beyond what is directly supported by the quotes provided and cited about **{company_name}**.

Source and Accuracy Requirements:
*   **Accuracy**: Every quote must be verbatim, correctly attributed to the speaker (with title) from **{company_name}**, and include precise source details (document/event, date, page/time if possible). Silently omit quotes if not verifiable after exhaustive search.
*   **Traceability**: Each quote's origin must be confirmed by an inline citation [SSX] corresponding to the final Sources list.
*   **Source Quality**: Use only official communications from **{company_name}** (Annual/Integrated reports, earnings call transcripts, official IR presentations/webcasts, company-published interviews). Avoid secondary reporting of quotes unless the secondary source itself is grounded.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

def get_strategy_research_prompt(
    company_name: str,  # Target Company
    language: str = "English",
    ticker: Optional[str] = None,
    industry: Optional[str] = None,
    context_company_name: str = "NESIC"  # Analyzing Company - default added back
):
    """
    Generates a generalized prompt for creating a comprehensive 3-Year "Strategy Research"
    Action Plan for {company_name} (Target Company), leveraging the dynamically and
    thoroughly researched capabilities of {context_company_name} (Analyzing Company),
    with enhanced entity focus and analytical depth.
    """
    context_str = f"**{company_name}**" # Target Company context string
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    # Use the updated FINAL_REVIEW_INSTRUCTION which includes the alignment check
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(
        company_name=company_name,
        context_company_name=context_company_name # Pass context company name for review instruction
        )
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)
    # NEW: Format the ENHANCED context company capabilities instruction
    formatted_analyzing_company_capabilities = ANALYZING_COMPANY_CAPABILITIES_INSTRUCTION.format(
        context_company_name=context_company_name, # Analyzing Company
        company_name=company_name # Target Company
    )
    
    # Add enhanced time period and table formatting instructions
    enhanced_time_and_formatting = textwrap.dedent(f"""\
    **Critical Time Period and Formatting Clarity**:
    
    1. **Financial & Trend Data**:
       * Always use the most recent **completed fiscal years** with available data for {company_name}. Clearly label specific fiscal years in all tables and text (e.g., "FY2023, FY2024, FY2025" rather than just "last 3 years").
       * Include end dates where appropriate (e.g., "FY2025 ending March 31, 2026").
       * For forecasts or targets, clearly state the timeframe with specific end years.
    
    2. **Table Formatting Excellence**:
       * Every table must have consistent column counts across all rows.
       * Every row must begin and end with pipes (|).
       * Use a single hyphen (-) for missing values only when needed for table structure and confirmed missing after thorough research.
       * Align numerical data for readability (right-aligned).
       * Include unit descriptions (e.g., "Revenue (USD M)") in column headers.
       * Ensure all tables have appropriate header separator lines.
       * Maintain proper spacing between cell content and pipe separators (e.g., `| Cell content |` not `|Cell content|`).
    
    3. **Data Point Precision**:
       * Each financial figure must be accompanied by currency and timeframe.
       * Each date must be in consistent format (YYYY-MM-DD or explicit period end dates).
       * Each percentage should include the % symbol.
       * Each source citation [SSX] must correspond to a valid entry in the final Sources list.
    
    4. **Silent Omission Implementation**:
       * After thorough research, silently omit data points about {company_name} that cannot be verified with grounding URLs.
       * Never explain data is "missing" or "not available" - simply exclude the unverifiable point.
       * For key sections where no verifiable data exists, retain the headings but provide minimalist content based only on verified information.
    """)

    prompt = f"""

**CRITICAL FOCUS**: This Strategy Research is *exclusively* about the specific Target Company: {context_str}. Verify the identity of the Target Company for all sourced information [SSX]. Do not include unrelated entities. This plan leverages public data about the Target Company ({company_name}) to inform a strategic account plan for the Analyzing Company ({context_company_name}).

# Comprehensive 3-Year Strategy Research & Action Plan: Targeting {company_name} for {context_company_name}

## Executive Summary

This strategic account plan provides a comprehensive 3-year engagement roadmap for **{context_company_name}** to approach **{company_name}** as a target client. The analysis examines the target company's strategic priorities, growth initiatives, organizational challenges, and market position to identify specific opportunities where {context_company_name}'s capabilities align with {company_name}'s stated needs and objectives.

Objective: Create a detailed, data-driven, and highly specific Strategy Research action plan for engaging the Target Company ({company_name}) over the next three fiscal years (e.g., FY2025-FY2027). This plan must be based *exclusively* on verifiable information about the Target Company ({company_name}) obtained through grounded sources [SSX]. Crucially, the analysis must identify **specific, non-generic opportunities** where the **thoroughly researched capabilities, named solutions, and verifiable strengths** of the Analyzing Company ({context_company_name}), determined via mandatory preliminary research (see instructions below), align with the Target Company's ({company_name}) stated needs, initiatives, or challenges. Focus strictly on the Target Company: {context_str}.

Target Audience Context: This plan is for internal use by the Analyzing Company's ({context_company_name}) sales, pre-sales, marketing, and strategy teams. Recommendations must be concrete and actionable, highlighting potential alignments between the Target Company's ({company_name}) verified situation [SSX] and the specifically identified capabilities of the Analyzing Company ({context_company_name}). The goal is a practical, differentiated roadmap, not a generic overview. {formatted_audience_reminder}

{get_language_instruction(language)}

{formatted_analyzing_company_capabilities} # Instructs LLM on mandatory, in-depth research & application of {context_company_name} capabilities

Research Requirements (Target Company - {company_name}):
*   Use only data about the **Target Company ({company_name})** validated through Gemini grounding URLs [SSX]. Perform exhaustive checks across multiple primary sources (latest reports, filings, presentations, official website) before silently omitting unverified data about {company_name}.
*   Every fact, figure, stated initiative, or challenge pertaining to the **Target Company ({company_name})** must be backed by an inline citation [SSX]. Silently omit any unverified points about {company_name}.
*   Use **perfect Markdown tables** for presenting data related to {company_name}. Verify data accuracy against sources. Use '-' for missing data points only if structurally necessary and confirmed absent in source for {company_name}.
*   Focus on extracting actionable intelligence about **{company_name}** that informs specific, tailored strategic engagement possibilities for **{context_company_name}**. Analyze the *implications* of the data deeply.

{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on {company_name}'s reports, financials, strategy docs
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION} # Focus analysis on identifying needs {context_company_name} could meet & explaining *why* with specifics
{enhanced_time_and_formatting}

{formatted_additional_instructions}

## Executive Summary
*   **Strategic Opportunity Assessment**: Provide a concise 300-400 word executive summary of the strategic opportunity **{company_name}** represents for **{context_company_name}** [SSX]
*   **Key Engagement Opportunities**: Identify the 3-5 most significant alignment areas between {company_name}'s needs and {context_company_name}'s capabilities [SSY]
*   **Account Priority Summary**: Summarize {company_name}'s strategic importance, relationship potential, and revenue opportunity for {context_company_name} [SSZ]
*   **Competitive Positioning Insights**: Highlight {context_company_name}'s competitive advantages and differentiation opportunities with this target [SSW]
*   **3-Year Engagement Priorities**: List the top 3 strategic priorities for engaging {company_name} over the planning period [SSV]

## 1. Target Company Profile ({company_name})
    *   **Company Name**: {company_name} [SSX]
    *   **Ticker**: {ticker or "N/A"} [SSX]
    *   **Industry & Sub-sector**: {industry or "N/A"} [SSX] (Note key sub-sectors if relevant and verifiable [SSY])
    *   **Headquarters**: [Full Registered HQ Address] [SSX]
    *   **Current CEO**: [Full Name and Title] [SSX] (Verify latest)
    *   **Key Executives Relevant to Strategy/IT/Operations**: (List names/titles if verifiable, e.g., CIO, CTO, CDO, CFO, COO, Head of Digital, Key BU Leaders) [SSY]
    *   **Approximate Employee Range/Number**: [Most recent figure with date] [SSX]
    *   **Core Business Summary**: Summarize main operations, key products/services, primary customer segments, and main markets based on latest official reports for {company_name} [SSX].
    *   *(Note: Avoid speculation on {context_company_name}-{company_name} relationship history unless verifiable via grounding URLs [SSZ]. Focus analysis on {company_name}.)*

## 2. Target Company Revenue Analysis & Growth Drivers ({company_name})
    *   Present Revenue for {company_name} for the last 3 full fiscal years (FY2023, FY2024, FY2025) in a **perfectly formatted Markdown table**, specifying currency (e.g., JPY Millions) [SSX]. Calculate YoY Growth Rate (%). Verify data. Use '-' for missing data points only if needed for table structure.
        
        **Example revenue table format (replace with actual data)**:
        
        | Metric                  | FY2023  | FY2024  | FY2025  | Source(s) |
        |-------------------------|---------|---------|---------|-----------|
        | Total Revenue (JPY M)   | 123,456 | 135,789 | 145,678 | [SS1]     |
        | YoY Growth Rate (%)     | -       | 10.0%   | 7.3%    | (Calc)    |
    *   Identify key business segments or geographic regions driving **{company_name}**'s revenue growth or decline, based on sourced segment data [SSY]. Analyze trends using specific figures (% change, contribution shift) from the latest available data [SSZ]. Explain the *reasons* for these trends if stated in sources [SSW].
    *   **Strategic Implications for {context_company_name}**: Where are the verifiable growth areas within {company_name} [SSY, SSZ] that align with {context_company_name}'s specific, researched capabilities and target industries? (e.g., "Target's growth in Sector X [SSY] aligns with Analyzing Co.'s 'Solution Suite for Sector X'"). Where are the verifiable challenges (e.g., declining segment needing efficiency gains [SSW]) that {context_company_name}'s specific solutions (e.g., "Named Automation Platform Y," "Specific Managed Service Z") could address? Explain the connection clearly and specifically.

## 3. Target Company Financial Performance & Investment Capacity ({company_name})
    *   Present Net Income (Attributable to Parent), Operating Margin (%), and Capital Expenditures (CapEx) for {company_name} for the last 3 full fiscal years (FY2023, FY2024, FY2025) in a **perfectly formatted Markdown table** [SSX, SSY, SSZ]. Verify data. Use '-' for missing data points only if needed for table structure.
        
        **Example financial table format (replace with actual data)**:
        
        | Metric                           | FY2023   | FY2024   | FY2025   | Source(s) |
        |----------------------------------|----------|----------|----------|-----------|
        | Net Income (Parent) (JPY M)      | 12,345   | 14,567   | 15,789   | [SS1]     |
        | Operating Margin (%)             | 12.5%    | 13.2%    | 14.0%    | [SS2]     |
        | Capital Expenditures (CapEx) (JPY M)| 8,765 | 9,876    | 11,234   | [SS3]     |
    *   Note key profitable divisions/segments of {company_name} if identifiable from sourced data [SSW]. Analyze trends in profitability and investment levels, explaining drivers if possible [SSX, SSY, SSZ]. Look for commentary on investment priorities [SSV].
    *   **Strategic Implications for {context_company_name}**: Does {company_name}'s financial health [SSX] and CapEx trend/priorities [SSZ, SSV] suggest capacity and appetite for significant strategic investments aligning with {context_company_name}'s high-value offerings (e.g., large DX/SI projects)? Are margin pressures [SSY] creating a verifiable need for specific cost optimization solutions (e.g., "{context_company_name}'s Managed Cloud Cost Optimization Service," "{context_company_name}'s RPA Implementation for Finance Processes") from {context_company_name}'s researched portfolio? Justify the assessment with evidence.

## 4. Target Company Strategic Initiatives & Specific {context_company_name} Alignments ({company_name})
    *   List **{company_name}**'s major publicly stated strategic initiatives for the next 1-3 years (from latest MTP, Annual Report, IR presentations, CEO messages). Include focus areas (e.g., Digital Transformation, Sustainability/ESG, Supply Chain Resilience, New Product/Market Development, Workforce Upskilling), specific verifiable goals (quantitative preferred), timelines, and investment figures (with currency) if available [SSX]. Use detailed bullet points for 3-5 key initiatives:
        *   **Initiative 1**: [Name/Focus, e.g., "Sustainability Program: Carbon Neutrality by 2040"] [SSX]
            *   Stated Goal: [e.g., Reduce Scope 1 & 2 emissions by 50% by 2030; Source 100% renewable energy] [SSX]
            *   Key Actions Mentioned: [e.g., Investing in energy-efficient manufacturing tech, deploying smart building solutions, improving supply chain sustainability reporting] [SSY]
            *   **Potential {context_company_name} Alignment**: [Explain *specifically* how {context_company_name}'s researched capabilities fit. e.g., "If {context_company_name} offers Green IT solutions, IoT for energy monitoring (like 'Smart Facility Monitor X'), or Sustainability Data Platform integration services, these directly support stated actions [SSY]. Highlight specific relevant offerings identified in preliminary research."]
        *   **Initiative 2**: [Name/Focus, e.g., "Next-Generation Product Development using AI"] [SSZ]
            *   Stated Goal: [e.g., Launch 3 new AI-enabled products in Sector Y by FY2027] [SSZ]
            *   Technology Focus: [e.g., Building internal AI/ML capabilities, potentially partnering for specific algorithms] [SSW]
            *   **Potential {context_company_name} Alignment**: [e.g., "{context_company_name}'s 'AI Development Platform' or 'AI Consulting Services' could accelerate this. If {context_company_name} has AI partnerships or specific industry AI solutions (identified in research), these create strong alignment. SI capabilities needed for integration."]
        *   *(List 3-5 major verifiable initiatives from latest sources for {company_name}, ensuring goals and actions are captured)*
    *   For each verifiable initiative of {company_name}, explicitly and specifically state how the researched **{context_company_name}** capabilities, **named solutions**, and **verifiable strengths** could provide unique value and support its stated goals. Demonstrate clear understanding of both companies.

## 5. Target Company Decision-Making Structure & Key Stakeholders ({company_name})
    *   Outline **{company_name}**'s organizational structure relevant to IT / DX / Strategic Procurement decisions (e.g., Role and influence of specific C-level execs like CIO/CTO/CDO/CFO, structure of IT department, existence and mandate of DX-focused teams or committees, BU autonomy) based on latest verifiable sources [SSX]. Note location of official org charts if found [SSY].
    *   Identify key executives (names, current titles) within **{company_name}** responsible for overall strategy, finance (CFO), IT/Digital (CIO/CTO/CDO), operations (COO), procurement, and heads of major business units that are likely targets for {context_company_name}'s solutions. Use latest verifiable management structure information [SSY]. Verify titles meticulously.
    *   Analyze potential decision-making processes for different types of solutions (e.g., "Major platform decisions likely involve cross-functional committee including IT, Finance, and relevant BUs, requiring C-level sign-off [SSX]. Smaller operational tech upgrades may be driven at BU level with IT validation [SSY]"). Consider influence maps if possible based on roles/structure.

## 6. Target Company Critical Business Challenges & Specific {context_company_name} Solutions ({company_name})
    *   Enumerate **{company_name}**'s major business challenges as explicitly stated in recent official sources (e.g., Annual Report risk factors, MTP context analysis, management commentary). Categorize if possible (e.g., Market Competition, Operational Inefficiency, Technological Debt, Regulatory Compliance, Talent Acquisition/Retention, Cybersecurity Threats, Supply Chain Disruptions) [SSX].
        *   **Challenge 1**: [e.g., "Intensifying competition from digital-native startups in core market segment"] [SSX] -> **Potential {context_company_name} Solution**: [Be specific & link to researched capability. e.g., "{context_company_name}'s 'Digital Customer Experience Platform' combined with its 'Agile Development Services' could help {company_name} rapidly launch competing digital offerings. This leverages {context_company_name}'s strength in [Specific Strength]."]
        *   **Challenge 2**: [e.g., "Ensuring compliance with upcoming data privacy regulation XYZ"] [SSY] -> **Potential {context_company_name} Solution**: [e.g., "{context_company_name}'s 'Data Governance & Compliance Consulting Service', potentially including implementation support for specific tools they partner with (if known), directly addresses this regulatory need."]
        *   **Challenge 3**: [e.g., "Skills gap in workforce for adopting new digital tools"] [SSZ] -> **Potential {context_company_name} Solution**: [e.g., "While {context_company_name} might not offer training directly, its 'Managed Services for Tool X' could reduce the immediate need for internal expertise. Alternatively, {context_company_name}'s SI services often include knowledge transfer components."]
        *   *(List 3-5 key verifiable challenges for {company_name} from latest sources)*
    *   For each verifiable challenge of {company_name}, propose **specific, relevant {context_company_name} solutions or service categories** (referencing the specific offerings identified during preliminary research) that directly address the verified problem. Clearly explain the value proposition and why it's a better fit than a generic approach.

## 7. Target Company Technology Environment & Future Roadmap ({company_name})
    *   Summarize **{company_name}**'s known current technology landscape (e.g., primary ERP system, main cloud provider(s), key operational technology platforms, stated use of specific SaaS tools) *if explicitly mentioned* in recent, verifiable sources [SSX]. Note key stated technology vendor relationships or strategic partnerships [SSY].
    *   Synthesize **{company_name}**'s likely technology investment priorities for the next 3 years (FY2025-FY2027) based on stated initiatives (Sec 4), investment commentary (Sec 3), and challenges (Sec 6). Examples: [Be specific based on findings] Cloud platform rationalization [SSX], Investment in data warehousing/lakes [SSY], Implementing specific cybersecurity framework [SSZ], Automation technologies (RPA/AI) in Function X [SSW], Upgrading specific core business application [SSV]. Use latest verifiable information.
    *   **Strategic Implications for {context_company_name}**: How does {company_name}'s apparent tech environment and roadmap [SSX, SSY] align or conflict with {context_company_name}'s core technology expertise, key partnerships (identified in preliminary research), and flagship solution portfolio? Identify specific areas of strong synergy (e.g., "{company_name}'s focus on Azure [SSX] aligns perfectly with {context_company_name}'s Premier Azure Partner status") and potential gaps {context_company_name} might need to address (e.g., via partnerships) to provide comprehensive solutions for {company_name}.

## 8. Strategic Engagement Plan Outline (FY2025–2027)
    *   Provide a high-level quarterly engagement plan concept for {context_company_name} to approach {company_name}. Focus on **strategic themes** derived from {company_name}'s verified needs and initiatives, directly aligned with **specific, researched {context_company_name} capabilities/solutions**. Use a **perfectly formatted Markdown table**. Verify data links. Prioritize themes based on potential impact and alignment strength.
        
        **Example engagement plan table format (replace with actual data)**:
        
        | Period         | Engagement Theme      | {context_company_name} Solutions | Target Stakeholder    | Citation Source | Business Goal       |
        |----------------|----------------------|----------------------------------|----------------------|----------------|---------------------|
        | FY2025 Q1      | DX Strategy Alignment | 'DX Framework', Case Studies     | CIO, Digital Head    | Initiative [SS1]| Establish credibility |
        | FY2025 Q2      | Cloud Security        | 'Cloud Security Suite', Assessment| CISO, Architecture   | Challenge [SS2] | Security partnership |
        | FY2025 Q3      | Enable Initiative Y   | 'Platform Z' demo and workshop   | BU Lead, Project Lead| Initiative [SS3]| Identify pilot      |
        | FY2025 Q4      | Efficiency ROI        | 'Managed Service ABC' Assessment | CFO, IT Operations   | Challenge [SS4] | Build financial case|
        | FY2026 Q1-Q2   | Pilot Projects        | Detailed SOWs for solutions      | Decision Makers      | FY2025 outcomes  | Secure initial wins |
        | FY2026 Q3-Q4   | Execution & Expansion | Delivery, QBRs, upsell services  | Project Sponsors     | Pilot success  | Demonstrate value   |
        | FY2027 onwards | Strategic Partnership | Joint roadmap, innovation plans  | C-Suite, Strategy    | Track record   | Preferred partner   |

## 9. Competitive Landscape ({company_name}'s Perspective) & {context_company_name}'s Differentiated Positioning
    *   Identify **{company_name}**'s existing major IT service providers, consultants, system integrators, or key technology vendors *if explicitly mentioned* in verifiable, recent sources [SSX]. Note the specific scope of their engagement if stated [SSY].
    *   Analyze (based *only* on verifiable public information about {company_name}'s vendors [SSX] and the **specific, researched capabilities/strengths** of {context_company_name}):
        *   Where does {context_company_name} possess a **demonstrable, specific differentiator** against these incumbents *in the context of {company_name}'s identified needs and initiatives*? (e.g., "{context_company_name}'s 'Solution A' directly addresses {company_name}'s Initiative X [SSX], whereas Incumbent B focuses elsewhere," "{context_company_name} has certified expertise in Technology Y [based on research] which is critical for {company_name}'s roadmap [SSY], unlike Incumbent C," "{context_company_name}'s local support model better fits {company_name}'s operational footprint [SSZ]").
        *   Where might incumbents hold advantages ({context_company_name} needs to strategize against)? (e.g., Incumbent's long-term contract, sole-source technology).
    *   Base the analysis strictly on evidence. Avoid speculation. Silently omit if no verifiable incumbent information is found for {company_name}.

## 10. Success Metrics & Potential KPIs (for {context_company_name})
    *   Define 3-5 specific, measurable Key Performance Indicators (KPIs) for **{context_company_name}**'s engagement with **{company_name}** over the 3 years (FY2025-FY2027). These should be *internal* {context_company_name} goals reflecting the strategic opportunities identified through verifiable data about {company_name} and the proposed engagement plan.
        *   **KPI 1: Strategic Initiative Alignment**: Number of qualified opportunities pipeline generated directly mapped to {company_name}'s top 3 strategic initiatives (Sec 4) where {context_company_name} has a researched, differentiated offering. (Target: X opps by FY2027).
        *   **KPI 2: Solution Portfolio Penetration**: Revenue generated from {context_company_name}'s *strategic/high-priority solution categories* (identified during preliminary research) within {company_name}. (Target: Achieve Y% of total account revenue from strategic solutions by FY2027).
        *   **KPI 3: Executive Relationship Depth**: Number of C-level / Key Stakeholder (Sec 5) meetings secured per quarter focused on strategic alignment (not just operational updates). (Target: Avg Z per quarter).
        *   **KPI 4: Competitive Displacement Rate**: Win rate (%) in opportunities where {context_company_name} is directly competing against a major incumbent identified in Sec 9 for a strategic project related to {company_name}'s needs. (Target: > B%).
        *   **KPI 5: Pilot-to-Production Conversion**: Conversion rate (%) of successful pilot projects (addressing needs in Sec 4/6) into larger-scale production deployments or ongoing managed services. (Target: > C%).
    *   Briefly explain the rationale: Why are these specific KPIs the best indicators of {context_company_name}'s success in executing this data-driven strategy for {company_name}, based on the analysis?

## 11. Final 3-Year Strategy Research Summary ({company_name} Focus, {context_company_name} Opportunity)
    *   Provide a concise concluding single paragraph (~300–500 words) synthesizing the most critical findings about the **Target Company ({company_name})** (their key strategic imperatives [SSX], major investment areas [SSY], significant business/technology challenges [SSZ], financial context [SSW]) and reiterating the **highest-priority, most specific alignment opportunities** for the **Analyzing Company ({context_company_name})**. Base this summary *only* on the verifiable data presented about {company_name} and the **specific, researched capabilities and named solutions** of {context_company_name}. Use latest available data. Incorporate key quantitative points where impactful.
    *   Emphasize the data-driven nature of the identified opportunities and construct a compelling narrative for *why* **{context_company_name}** is uniquely positioned to be a strategic partner for **{company_name}**. Example: "Target Company {company_name}'s public commitment to Initiative X [SSX], coupled with their reported struggle with Challenge Y [SSY], creates a clear mandate for a solution like Analyzing Company {context_company_name}'s 'Specific Platform Z'. Our research indicates {context_company_name}'s unique strength in [Verifiable Strength] further differentiates this offering from known competitors [SSZ]. The proposed engagement focuses on demonstrating this specific value proposition early (FY2025 Q2) to capture this strategic opportunity..."
    *   Avoid introducing new data or internal {context_company_name} assumptions not explicitly linked back to the verified {company_name} information [SSX] and the specific, researched {context_company_name} capabilities. Conclude with a clear, ambitious, yet realistic statement of the overall strategic objective for {context_company_name} regarding {company_name} over the next three years.

Source and Accuracy Requirements:
*   **Accuracy**: All data about the **Target Company ({company_name})** must be grounded in official records [SSX] and reflect the latest available verifiable information. The application of the **Analyzing Company's ({context_company_name})** capabilities must be specific, non-generic, and based on diligent preliminary research of its actual offerings/strengths. Silently omit unverified data about {company_name} after exhaustive search. Verify table data meticulously.
*   **Traceability**: Each fact or figure about the **Target Company ({company_name})** must include an inline citation [SSX], linking to final source(s).
*   **Single-Entity Coverage**: Strictly reference the **Target Company ({company_name})**'s data; omit any similarly named entities. Clearly distinguish between the Target Company and the Analyzing Company.

{formatted_completion_template}
{formatted_final_review} # Ensure this uses the updated version
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# News Analysis Prompt
def get_news_analysis_prompt(company_name: str, language: str = "Japanese", ticker: Optional[str] = None, industry: Optional[str] = None, context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing latest business-relevant news about a company with enhanced entity focus."""
    context_str = f"**{company_name}**"
    if ticker: context_str += f" (Ticker: {ticker})"
    if industry: context_str += f" (Industry: {industry})"

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker=ticker or "N/A", industry=industry or "N/A")
    formatted_research_depth = RESEARCH_DEPTH_INSTRUCTION.format(company_name=company_name)
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_final_source_list = FINAL_SOURCE_LIST_INSTRUCTIONS_TEMPLATE.format(language=language)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    # Calculate 6-month lookback period (using current date concept)
    date_range = "past 6 months"

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: {context_str}. Verify the identity of the company for all sourced information. Do not include unrelated entities or similarly named companies.

# Comprehensive Business Intelligence News Analysis for {company_name}

## Executive Summary

This business intelligence analysis examines recent news and developments related to **{company_name}** to provide strategic insights for {context_company_name}'s business development and competitive intelligence. The report analyzes relevant news across multiple categories including HR & organizational changes, business operations, financial performance, technology initiatives, and strategic partnerships to identify opportunities and assess market developments.

Objective: As a business intelligence analyst for **{context_company_name}** (NEC Networks & System Integration Corporation), fetch and analyze the latest business-relevant news about **{company_name}** from the {date_range}. Focus strictly on {context_str}.

Target Audience Context: This analysis is designed for **{context_company_name}** sales, strategy, and leadership teams requiring actionable intelligence for partnership evaluation, competitive assessment, and market opportunity identification. {formatted_audience_reminder}

{get_language_instruction(language)}

**{context_company_name} BUSINESS CONTEXT:**
Focus on news relevant to IT services, system integration, digital transformation, enterprise solutions, technology infrastructure, and corporate business operations. Filter through the lens of what would be valuable intelligence for a technology services company like {context_company_name}.

**FILTERING CRITERIA:**
✅ INCLUDE: Business operations, financial performance, technology developments, partnerships, organizational changes, market activities, strategic initiatives, product launches, acquisitions, regulatory changes, industry positioning
❌ EXCLUDE: Sports team performance, entertainment ventures, personal lifestyle news of executives (unless directly impacting business operations), celebrity endorsements, non-business social activities

Research Requirements:
Conduct exhaustive research using reputable business news sources, financial publications, industry reports, and official company announcements for **{company_name}**. Each news item must include an inline citation [SSX] with specific dates and source references. Use **perfect Markdown formatting**. Only include verifiable, business-relevant news items.
{HANDLING_MISSING_INFO_INSTRUCTION}
{formatted_research_depth} # Focus on news sources, press releases, financial reports
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## Executive Summary
*   **News Intelligence Assessment**: Provide a concise 250-300 word executive summary of the most significant recent developments affecting **{company_name}** [SSX]
*   **Key Business Impact Areas**: Identify the 3-5 most important news categories and their strategic implications for {company_name} [SSY]
*   **Market Opportunity Summary**: Summarize opportunities and threats for {context_company_name} based on {company_name}'s recent activities [SSZ]
*   **Competitive Intelligence Insights**: Highlight competitive positioning changes, market dynamics, and strategic shifts [SSW]
*   **{context_company_name} Action Priorities**: List the top 3 immediate actions {context_company_name} should consider based on the news analysis [SSV]

### Key Trends & Insights
Brief analysis of major trends observed in **{company_name}**'s activities over the past 6 months, highlighting the most significant developments and their strategic implications [SSX]. Include specific dates and quantified impacts where available [SSY].

### Strategic Implications for {context_company_name}
- **Opportunities**: Potential partnership, collaboration, or business opportunities identified based on {company_name}'s recent activities and strategic direction [SSX]
- **Threats**: Competitive threats or market challenges to monitor that could impact {context_company_name}'s positioning [SSY]
- **Recommendations**: 2-3 specific actionable recommendations for {context_company_name} leadership based on the news analysis [SSZ]

---

## Detailed News Analysis

### HR & Organization
For each significant news item in this category, provide:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: 2-3 sentence overview focusing on business impact for {company_name} [SSX]
- **Business Relevance**: How this affects {company_name}'s operations, strategy, or market position [SSY]
- **{context_company_name} Action Items**: 1-2 specific, actionable recommendations for {context_company_name} teams [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

### Business Operations & Strategy
For each significant news item in this category, provide:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: 2-3 sentence overview focusing on business impact for {company_name} [SSX]
- **Business Relevance**: Strategic implications for {company_name}'s market positioning and operations [SSY]
- **{context_company_name} Action Items**: 1-2 specific, actionable recommendations for {context_company_name} teams [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

### Financial Performance
For each significant news item in this category, provide:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: Include specific financial figures with currency and reporting periods [SSX]
- **Business Relevance**: Impact on {company_name}'s financial health and investment capacity [SSY]
- **{context_company_name} Action Items**: How this affects potential business opportunities or risks [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

### Technology & Innovation
For each significant news item in this category, provide:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: Focus on technological developments and innovation initiatives by {company_name} [SSX]
- **Business Relevance**: Technology trends and competitive positioning implications [SSY]
- **{context_company_name} Action Items**: Opportunities for collaboration or competitive response [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

### Partnerships & Acquisitions
For each significant news item in this category, provide:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: Details of M&A activity, partnerships, or strategic collaborations [SSX]
- **Business Relevance**: Strategic implications for {company_name}'s capabilities and market reach [SSY]
- **{context_company_name} Action Items**: Partnership opportunities or competitive considerations [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

### Market & Regulatory
For each significant news item in this category, provide:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: Market developments, regulatory changes, or industry positioning updates [SSX]
- **Business Relevance**: Impact on {company_name}'s operating environment and compliance requirements [SSY]
- **{context_company_name} Action Items**: Strategic or operational adjustments needed [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

### Others
For any remaining business-relevant news that doesn't fit the above categories:
- **Impact Level**: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
- **Summary**: Brief overview of the development [SSX]
- **Business Relevance**: Why this matters for {company_name} [SSY]
- **{context_company_name} Action Items**: Recommended actions for {context_company_name} [SSZ]
- **Source**: Publication name, YYYY-MM-DD [SSX]

## General Discussion
Provide a concluding single paragraph (300-500 words) that synthesizes the key findings from the news analysis regarding **{company_name}**. Assess the overall trajectory of the company based on recent developments, identify the most significant opportunities and risks for {context_company_name}, and provide strategic recommendations for engagement. Use inline citations to link back to specific news items [SSX, SSY]. Structure the discussion by starting with an overall assessment of {company_name}'s recent activities, discussing key strategic implications, and concluding with prioritized recommendations for {context_company_name} from a Japanese business perspective.

**IMPACT SCORING GUIDELINES:**
- **🔴 HIGH**: Major strategic changes, large acquisitions, significant financial events, key technology breakthroughs, major leadership changes
- **🟡 MEDIUM**: Important operational changes, medium partnerships, notable product launches, moderate financial updates
- **🟢 LOW**: Minor updates, small partnerships, routine announcements, incremental improvements

**CRITICAL INSTRUCTIONS:**
- Sort news within each category by impact level (HIGH first, then MEDIUM, then LOW)
- Prioritize more recent news when impact levels are equal
- Each news item must include impact score (🔴🟡🟢) and {context_company_name} Action Items
- Include publication date in format: Source Name, YYYY-MM-DD
- If no significant business news found, return: "No significant business news found for {company_name} in the past 6 months [SSX]."

Source and Accuracy Requirements:
*   **Accuracy**: All news items must be verifiable and current for **{company_name}**. Specify exact dates, financial figures with currency, and impact levels. Silently omit unverified news after exhaustive search.
*   **Traceability**: Every news item must include an inline citation [SSX] corresponding to the final Sources list.
*   **Source Quality**: Use reputable business publications, financial news sources, official company announcements, and industry reports only if grounded by search results.

{formatted_completion_template}
{formatted_final_review}
{formatted_final_source_list}
{formatted_base_formatting}
"""
    return prompt

# SFDC Analysis Prompt
def get_sfdc_analysis_prompt(company_name: str, language: str = "Japanese", context_company_name: str = "NESIC"):
    """Generates a prompt for analyzing SFDC/CRM transaction data with enhanced entity focus and comprehensive table structures."""
    
    # Language terms dictionary
    lang_terms = {
        "Japanese": {
            "error_not_found": f"提供されたJSONファイルに該当する企業「{company_name}」の有効なデータ（アカウント情報または関連する取引情報）が見つかりません。JSONファイルの内容を確認するか、正確な企業名（JSON内の 'Name' または 'CT_NameAbbreviation__c' と完全に一致する）を指定してください。",
            "error_json_format": "提供されたファイルは有効なJSON形式ではないか、必須のキー（'accounts', 'opportunities'）が欠落しています。",
            "error_title": "エラー",
            "no_won_deals_found": "指定された期間内に分析対象の受注済み取引（IsWon = true）が見つかりませんでした。分析はアカウント情報および全取引タイプ（受注、失注、進行中）に基づいて行われます。",
            "report_title": f"【{context_company_name}内部向け】 {company_name} 取引データ戦略分析レポート",
            "exec_summary": f"0. エグゼクティブサマリー（{context_company_name}向け）",
            "trend_analysis": "1. 主要受注実績 推移分析",
            "annual_revenue": "年間総受注金額",
            "annual_deal_count": "年間総受注件数",
            "avg_deal_size": "平均受注単価（年間）",
            "segment_analysis": "2. 受注セグメント分析",
            "sbu_division": "2.1 関連事業領域（アカウント情報ベース）",
            "service_product": "2.2 サービス・商材区分（取引の構造化データおよび案件名・タグからの推測）",
            "dx_strategic": "2.3 DX・戦略領域（取引の構造化データおよび案件名・タグからの推測）",
            "competitive_analysis": "2.4 競合・協業分析（アカウントタグ・取引履歴ベース）",
            "deal_characteristics": "3. 受注案件 特性分析",
            "avg_lead_time": "平均リードタイム（受注案件：クローズ日 - 作成日）",
            "deal_size_distribution": "受注案件規模 分布",
            "seasonal_patterns": "季節性・四半期パターン分析",
            "stage_analysis": "営業ステージ分析",
            "whitespace_analysis": f"4. ホワイトスペース分析 / 未開拓ポテンシャル（{context_company_name}視点）",
            "client_profile_context": "クライアントプロファイル・関心領域（アカウント情報・タグ）",
            "comparison_won_deals": "受注実績との比較",
            "identified_whitespace": f"特定されたホワイトスペース（{context_company_name}の潜在的機会）",
            "opportunity_matrix": "機会マトリックス（優先度×実現可能性）",
            "strategic_recommendations": f"5. 戦略的考察・推奨事項（{context_company_name}向け）",
            "strengths_leverage": "活用すべき強み（既存受注領域）",
            "focus_development": "注力・開発すべき領域（トレンド・ギャップ・ホワイトスペース）",
            "quick_wins": "短期的な機会",
            "efficiency_process": "営業プロセス効率化のヒント",
            "overall_posture": "全体的な戦略的位置づけ",
            "account_penetration": "6. アカウント浸透度分析",
            "penetration_metrics": "浸透度指標",
            "expansion_opportunities": "拡張機会",
            "visualization_suggestions": "7. 推奨される可視化（内部報告用）",
            "risks_mitigation": f"8. {context_company_name}にとってのリスクと軽減策",
            "based_on_general_knowledge": "(※市場の一般的知識および提供データに基づく考察)",
            "unit_deals": "件",
            "unit_currency": "円",
            "unit_days": "日",
            "year": "年度",
            "quarter": "四半期",
            "data_quality_limitations": "データ品質/分析の限界",
            "derived_from_close_date": " (CloseDateから導出)"
        },
        "English": {
            "error_not_found": f"Cannot find valid data (Account Information or related Opportunities) for the specified company '{company_name}' in the provided JSON file. Please check the JSON content or provide the correct company name (must exactly match 'Name' or 'CT_NameAbbreviation__c' in the JSON).",
            "error_json_format": "The provided file is not valid JSON or is missing required keys ('accounts', 'opportunities').",
            "error_title": "Error",
            "no_won_deals_found": "No completed ('Won' = true) deals were found for analysis within the specified period. Analysis will be based on Account Information and all opportunity types (won, lost, open).",
            "report_title": f"[Internal {context_company_name} Report] {company_name} Transaction Data Strategic Analysis",
            "exec_summary": f"0. Executive Summary (for {context_company_name})",
            "trend_analysis": "1. Key Won Deal Trend Analysis",
            "annual_revenue": "Total Annual Won Revenue",
            "annual_deal_count": "Total Annual Won Deal Count",
            "avg_deal_size": "Average Annual Won Deal Size",
            "segment_analysis": "2. Won Deal Segment Analysis",
            "sbu_division": "2.1 Related Business Areas (Based on Account Info)",
            "service_product": "2.2 Service/Product Categories (Inferred from Structured Opportunity Data, Deal Names & Tags)",
            "dx_strategic": "2.3 DX/Strategic Areas (Inferred from Structured Opportunity Data, Deal Names & Tags)",
            "competitive_analysis": "2.4 Competitive & Partnership Analysis (Based on Account Tags & Deal History)",
            "deal_characteristics": "3. Won Deal Characteristics Analysis",
            "avg_lead_time": "Average Lead Time (Won Deals: Close Date - Create Date)",
            "deal_size_distribution": "Won Deal Size Distribution",
            "seasonal_patterns": "Seasonal & Quarterly Pattern Analysis",
            "stage_analysis": "Sales Stage Analysis",
            "whitespace_analysis": f"4. White Space Analysis / Untapped Potential (from {context_company_name}'s Perspective)",
            "client_profile_context": "Client Profile & Interest Areas (Account Info & Tags)",
            "comparison_won_deals": "Comparison with Won Deal History",
            "identified_whitespace": f"Identified White Space (Potential {context_company_name} Opportunities)",
            "opportunity_matrix": "Opportunity Matrix (Priority × Feasibility)",
            "strategic_recommendations": f"5. Strategic Implications & Recommendations (for {context_company_name})",
            "strengths_leverage": "Strengths to Leverage (Existing Won Areas)",
            "focus_development": "Areas for Focus/Development (Trends, Gaps, White Space)",
            "quick_wins": "Potential Quick Wins",
            "efficiency_process": "Sales Process Efficiency Insights",
            "overall_posture": "Overall Strategic Posture Recommendation",
            "account_penetration": "6. Account Penetration Analysis",
            "penetration_metrics": "Penetration Metrics",
            "expansion_opportunities": "Expansion Opportunities",
            "visualization_suggestions": "7. Recommended Visualizations (for Internal Reporting)",
            "risks_mitigation": f"8. Risks & Mitigation Strategies (for {context_company_name})",
            "based_on_general_knowledge": "(Note: Observation based on general market knowledge and provided data)",
            "unit_deals": "deals",
            "unit_currency": "JPY",
            "unit_days": "days",
            "year": "FY",
            "quarter": "Q",
            "data_quality_limitations": "Data Quality/Analysis Limitations",
            "derived_from_close_date": " (Derived from CloseDate)"
        }
    }

    terms = lang_terms.get(language, lang_terms["English"])
    
    # NESIC capabilities context
    nesic_capabilities_context = textwrap.dedent(f"""\
    **{context_company_name} Capabilities & Strategic Context (Reference for Analysis):**

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

    *   **{context_company_name}'s Core Value Proposition & Strategic Approach (How We Succeed):**
        *   **Co-Creation Partnership:** We prioritize understanding client challenges deeply and collaborating closely to design and deliver the *optimal* solution, acting as a long-term strategic partner.
        *   **Leveraging NEC Group Strengths:** We uniquely integrate cutting-edge technologies (AI, biometrics, 5G/6G R&D, advanced analytics) and the broad solution portfolio of the NEC Corporation to deliver innovative and differentiated outcomes.
        *   **Ensuring Mission-Critical Reliability:** Decades of proven experience delivering and managing large-scale, complex systems for demanding clients, ensuring operational stability and resilience.
        *   **End-to-End Service Lifecycle:** Providing comprehensive support across the entire lifecycle, from initial consultation and design to implementation, management, and continuous improvement.
        *   **Vendor-Agnostic Integration Expertise:** Skillfully integrating best-of-breed solutions from a wide range of technology partners while ensuring interoperability and avoiding vendor lock-in where appropriate.

    *   **Key Differentiators (Why Choose {context_company_name}):**
        *   **NEC Group Technology Access:** Unique ability to incorporate world-class NEC R&D and specialized technologies.
        *   **Proven SI Track Record:** Unmatched experience in delivering complex, large-scale projects within the Japanese market.
        *   **Deep Networking & Security DNA:** Core technical leadership and heritage in designing and securing critical networks.
        *   **Nationwide Delivery & Support:** Robust, skilled service infrastructure across Japan for reliable installation, maintenance, and operational support.
        *   **Client-Centric Flexibility:** Combining structured methodologies with the agility to tailor solutions and engagement models to specific client needs.

    *   **Primary Target Segments:** Large Enterprises, Government Agencies & Public Sector Organizations, Telecommunications Carriers, Critical Social Infrastructure Providers.

    **(Note for AI Strategist:** Use this context to identify how {context_company_name}'s specific capabilities, approach, and differentiators can best address the target company's identified needs, challenges, and strategic initiatives from the provided JSON data. Frame opportunities by highlighting {context_company_name}'s unique value.)
    """)

    # Prepare formatted instruction blocks
    formatted_additional_instructions = ADDITIONAL_REFINED_INSTRUCTIONS.format(company_name=company_name, ticker="N/A", industry="N/A")
    formatted_final_review = FINAL_REVIEW_INSTRUCTION.format(company_name=company_name, context_company_name=context_company_name)
    formatted_completion_template = COMPLETION_INSTRUCTION_TEMPLATE.format(company_name=company_name)
    formatted_base_formatting = BASE_FORMATTING_INSTRUCTIONS.format(language=language)
    formatted_audience_reminder = AUDIENCE_CONTEXT_REMINDER.format(language=language)

    prompt = f"""

**CRITICAL FOCUS**: This entire request is *exclusively* about the specific entity: **{company_name}**. Verify the identity of the company for all sourced information from the JSON data. Do not include unrelated entities.



Comprehensive {context_company_name} Internal Strategic Analysis: {company_name} Transaction Data

Objective: You are an expert Senior Account Strategist and Data Analyst at **{context_company_name}**. Your objective is to meticulously analyze historical transaction data (provided as JSON in a `.txt` file) for the client **{company_name}** and generate a highly insightful, actionable strategic report **solely for internal {context_company_name} use**.

Target Audience Context: This analysis is for **{context_company_name}** sales, strategy, and account management teams requiring detailed insights for strategic engagement planning and business development. {formatted_audience_reminder}

{get_language_instruction(language)}

**Input Requirements:**
1. A `.txt` file containing structured JSON data with `accounts` and `opportunities` lists
2. Client Name: `{company_name}` (Must exactly match the `Name` or `CT_NameAbbreviation__c` in the account record within the JSON)
3. Output Language: `{language}`

**Target Audience:** Internal {context_company_name} Sales & Strategy Teams

--- {context_company_name} Capabilities Context (Reference for Mapping Opportunities) ---
{nesic_capabilities_context}
--- End {context_company_name} Capabilities Context ---

Research and Analysis Requirements:
*   **Data Source (ABSOLUTE):** Base **ALL** analysis **STRICTLY AND SOLELY** on the provided JSON data. No external web search.
*   **JSON Validation:** Validate JSON structure first. Must contain `accounts` and `opportunities` keys.
*   **Account Identification:** Find {company_name} by exact match with `accounts[*].Name` or `accounts[*].CT_NameAbbreviation__c`
*   **Won Deal Focus:** Primary analysis on opportunities where `IsWon == true` with valid `Amount > 0`
*   **Tag Processing:** Parse comma/semicolon-separated tag fields into individual items for analysis
*   **Missing Data Handling:** Handle null/invalid data gracefully - exclude from calculations but retain for counts where appropriate

{HANDLING_MISSING_INFO_INSTRUCTION}
{SPECIFICITY_INSTRUCTION}
{INLINE_CITATION_INSTRUCTION}
{ANALYSIS_SYNTHESIS_INSTRUCTION}

{formatted_additional_instructions}

## REQUIRED OUTPUT STRUCTURE ({language}):

# {terms['report_title']}

## Executive Summary

This comprehensive SFDC/CRM data analysis provides strategic insights into **{company_name}**'s transaction history, deal patterns, and business relationship dynamics from {context_company_name}'s perspective. The report examines won deal trends, service category performance, white space opportunities, and account penetration metrics to identify strategic engagement opportunities and optimize business development approaches.

## Executive Summary
*   **SFDC Data Intelligence Assessment**: Provide a concise 300-400 word executive summary of **{company_name}**'s transaction patterns and strategic relationship potential for **{context_company_name}** [SSX]
*   **Key Account Performance Insights**: Identify the 3-5 most significant findings from the deal history and account analysis [SSY]
*   **White Space Opportunity Summary**: Summarize the highest-priority untapped opportunities where {context_company_name} capabilities align with {company_name}'s needs [SSZ]
*   **Strategic Engagement Insights**: Highlight relationship depth, competitive positioning, and expansion potential [SSW]
*   **{context_company_name} Action Priorities**: List the top 3 immediate actions for optimizing the {company_name} relationship [SSV]

## {terms['exec_summary']}
*   Analyzed Account: {company_name}
*   Analysis Period: [Derive from earliest `CreatedDate` to latest `CloseDate` of relevant opportunities]
*   {terms['data_quality_limitations']}: [Briefly note significant data gaps or state "Data generally sufficient for analysis"]
*   Overall Won Business: [Total Won Revenue] {terms['unit_currency']} across [Total Won Deal Count] {terms['unit_deals']} (or state `{terms['no_won_deals_found']}`)
*   Key Trends (Won Deals): [1-2 sentences on revenue/deal trends or state limitations]
*   Dominant Won Segments: [Top 1-2 segments by revenue/volume from Section 2]
*   Top 1-2 Strategic Opportunities for {context_company_name}: [Link White Space analysis to specific {context_company_name} capabilities]
*   Key Challenges/Considerations for {context_company_name}: [Primary challenges based on data patterns]

## {terms['trend_analysis']}
*   **Analysis Basis:** Based on Won Deals (`IsWon == true`) with valid `Amount > 0` and valid `CloseDate`
*   **Historical Performance Table:**

    | {terms['year']} | {terms['annual_revenue']} ({terms['unit_currency']}) | {terms['annual_deal_count']} ({terms['unit_deals']}) | {terms['avg_deal_size']} ({terms['unit_currency']}) | YoY Growth (%) |
    |-----------------|-----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------|
    | FY2022          | [Total Revenue]                                     | [Total Deals]                                      | [Calculated Average]                               | -              |
    | FY2023          | [Total Revenue]                                     | [Total Deals]                                      | [Calculated Average]                               | [Calculated]   |
    | FY2024          | [Total Revenue]                                     | [Total Deals]                                      | [Calculated Average]                               | [Calculated]   |

*   **Trend Analysis:** [Analyze YoY growth patterns, identify acceleration/deceleration periods, note any significant changes in deal volume vs. deal size trends]
*   **Performance Insights:** [Link trends to business context - market conditions, company initiatives, competitive factors where identifiable from data]

## {terms['segment_analysis']}

### {terms['sbu_division']}
*   **Account Profile Summary:**
    *   Industry: [from `accounts[0].CT_IndustryName__c`]
    *   Market Segment: [from `accounts[0].CT_MarketSegmentName__c`]
    *   Account Size/Type: [Infer from available data]

*   **Client Interest & Focus Areas (parsed from account tags):**

    | Tag Category | Tag Items | {context_company_name} Relevance |
    |--------------|-----------|-----------------------------------|
    | Scenarios (`CT_f_scenarios__c`) | [List distinct items] | [Map to NESIC capabilities] |
    | Trends (`sci_ttag_trends__c`) | [List distinct items] | [Technology alignment assessment] |
    | Business Services (`sci_ttag_businessAndServices__c`) | [List distinct items] | [Service overlap analysis] |

### {terms['service_product']}
*   **Won Deal Service Category Analysis:**

    | Service/Product Category | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}) | Avg Deal Size ({terms['unit_currency']}) | % of Total Revenue | {context_company_name} Alignment |
    |--------------------------|-----------------------------------------------|----------------------------------------|-------------------------------------------|--------------------|-----------------------------------|
    | [Category 1]             | [Amount]                                      | [Count]                                | [Average]                                 | [Percentage]       | [Capability mapping]              |
    | [Category 2]             | [Amount]                                      | [Count]                                | [Average]                                 | [Percentage]       | [Capability mapping]              |
    | [Category 3]             | [Amount]                                      | [Count]                                | [Average]                                 | [Percentage]       | [Capability mapping]              |

*   **Category Performance Analysis:** [Identify top-performing categories, analyze deal size patterns, assess strategic importance for {context_company_name}]

### {terms['dx_strategic']}
*   **DX/Strategic Theme Analysis:**

    | DX/Strategic Theme | Total Won Revenue ({terms['unit_currency']}) | Won Deal Count ({terms['unit_deals']}) | Avg Deal Size ({terms['unit_currency']}) | Strategic Priority | {context_company_name} Differentiation |
    |--------------------|-----------------------------------------------|----------------------------------------|-------------------------------------------|--------------------|----------------------------------------|
    | [Theme 1]          | [Amount]                                      | [Count]                                | [Average]                                 | [High/Med/Low]     | [Specific advantages]              |
    | [Theme 2]          | [Amount]                                      | [Count]                                | [Average]                                 | [High/Med/Low]     | [Specific advantages]              |
    | [Theme 3]          | [Amount]                                      | [Count]                                | [Average]                                 | [High/Med/Low]     | [Specific advantages]              |

*   **Strategic Theme Insights:** [Analyze alignment with {context_company_name} core capabilities, identify growth themes, assess competitive positioning]

### {terms['competitive_analysis']}
*   **Competitive Landscape Indicators (from account tags and deal patterns):**

    | Indicator Type | Identified Elements | Impact on {context_company_name} | Strategic Response |
    |----------------|---------------------|-----------------------------------|-------------------|
    | Competitor Services (`sci_ttag_services__c`) | [List competitor services used] | [Threat/Opportunity assessment] | [Recommended approach] |
    | Technology Partners | [Identified from deal names/tags] | [Partnership vs. competition] | [Collaboration strategy] |
    | Service Gaps | [Areas without strong incumbents] | [Entry opportunity] | [Value proposition] |

## {terms['deal_characteristics']}
*   **Lead Time Analysis:**
    *   {terms['avg_lead_time']}: [Calculated average] {terms['unit_days']}
    *   Lead Time Distribution: [Range analysis - minimum, maximum, median]
    *   **Lead Time by Category:**

        | Category | Avg Lead Time ({terms['unit_days']}) | Sample Size | Insights |
        |----------|--------------------------------------|-------------|----------|
        | [Category 1] | [Days] | [Count] | [Pattern analysis] |
        | [Category 2] | [Days] | [Count] | [Pattern analysis] |

*   **Deal Size Distribution Analysis:**

    | Deal Size Range ({terms['unit_currency']}) | Number of Deals | % of Total Deals | Total Revenue | % of Total Revenue |
    |---------------------------------------------|----------------|------------------|---------------|-------------------|
    | < 1M | [Count] | [%] | [Amount] | [%] |
    | 1M - 5M | [Count] | [%] | [Amount] | [%] |
    | 5M - 10M | [Count] | [%] | [Amount] | [%] |
    | > 10M | [Count] | [%] | [Amount] | [%] |

*   **{terms['seasonal_patterns']}:**
    *   Quarterly Deal Closure Patterns: [Analyze CloseDate distribution by quarter]
    *   Revenue Seasonality: [Identify peak/trough periods]

*   **{terms['stage_analysis']}:**
    *   Current Pipeline Stage Distribution (for open opportunities)
    *   Historical Win/Loss Patterns by Stage

## {terms['whitespace_analysis']}

### {terms['client_profile_context']}
*   **Comprehensive Account Profile Matrix:**

    | Profile Dimension | Current Indicators | {context_company_name} Opportunity Assessment |
    |-------------------|-------------------|----------------------------------------------|
    | Client Scenarios (`CT_f_scenarios__c`) | [List items] | [Opportunity mapping] |
    | Technology Trends (`sci_ttag_trends__c`) | [List items] | [Technology alignment] |
    | Adopted IT Categories (`sci_ttag_adoptedItServiceCategory__c`) | [List items] | [Service expansion potential] |
    | Current Services (`sci_ttag_services__c`) | [List items] | [Competitive analysis] |
    | Service Categories (`CT_f_service_categories__c`) | [List items] | [Category penetration] |

### {terms['comparison_won_deals']}
*   **Won Deal Coverage Analysis:**
    *   Strong Performance Areas: [Categories with significant wins]
    *   Moderate Performance Areas: [Categories with some wins]
    *   Limited Engagement Areas: [Categories with few/no wins]

### {terms['identified_whitespace']}
*   **White Space Opportunity Matrix:**

    | White Space Area | Client Interest Indicators | Current {context_company_name} Presence | Opportunity Size | Implementation Difficulty | Priority Ranking |
    |------------------|----------------------------|------------------------------------------|------------------|--------------------------|-----------------|
    | [Area 1] | [Account tags supporting interest] | [None/Limited/Some] | [High/Med/Low] | [High/Med/Low] | [1-5] |
    | [Area 2] | [Account tags supporting interest] | [None/Limited/Some] | [High/Med/Low] | [High/Med/Low] | [1-5] |
    | [Area 3] | [Account tags supporting interest] | [None/Limited/Some] | [High/Med/Low] | [High/Med/Low] | [1-5] |

### {terms['opportunity_matrix']}
*   **Strategic Opportunity Prioritization:**

    | Opportunity | {context_company_name} Capability Match | Market Timing | Expected Deal Size | Competitive Intensity | Overall Priority |
    |-------------|------------------------------------------|---------------|-------------------|----------------------|-----------------|
    | [Opportunity 1] | [Strong/Moderate/Weak] | [Immediate/6-12mo/12mo+] | [High/Med/Low] | [High/Med/Low] | [P1-P3] |
    | [Opportunity 2] | [Strong/Moderate/Weak] | [Immediate/6-12mo/12mo+] | [High/Med/Low] | [High/Med/Low] | [P1-P3] |

## {terms['strategic_recommendations']}
*   **{terms['strengths_leverage']}:**
    *   Primary Strength Areas: [Top-performing categories with specific examples]
    *   Expansion Tactics: [How to grow within successful categories]
    *   Cross-Selling Opportunities: [Adjacent services to existing wins]

*   **{terms['focus_development']}:**
    *   High-Priority White Space: [Top-ranked opportunities from matrix]
    *   Capability Development Needs: [Skills/resources required]
    *   Partnership Requirements: [External alliances needed]

*   **{terms['quick_wins']}:**
    *   Immediate Opportunities: [0-6 month timeframe]
    *   Low-Hanging Fruit: [High probability, moderate impact]
    *   Pilot Project Candidates: [Testing ground for new services]

*   **{terms['efficiency_process']}:**
    *   Lead Time Optimization: [Based on characteristics analysis]
    *   Deal Size Optimization: [Strategies for larger deals]
    *   Win Rate Improvement: [Based on loss analysis if available]

*   **{terms['overall_posture']}:**
    *   3-Year Strategic Vision for {company_name}
    *   Annual Milestone Targets
    *   Success Metrics and KPIs

## {terms['account_penetration']}

### {terms['penetration_metrics']}
*   **Current Penetration Assessment:**

    | Metric | Current Status | Industry Benchmark | Target |
    |--------|---------------|-------------------|---------|
    | Service Category Coverage | [X/Y categories] | [Typical coverage] | [Goal] |
    | Annual Deal Velocity | [Deals/year] | [Typical velocity] | [Target] |
    | Average Deal Size Growth | [YoY %] | [Industry growth] | [Target] |
    | Client Stickiness | [Relationship duration] | [Typical duration] | [Goal] |

### {terms['expansion_opportunities']}
*   **Penetration Expansion Strategy:**
    *   Vertical Penetration: [Deeper into existing service areas]
    *   Horizontal Penetration: [New service categories]
    *   Relationship Expansion: [New stakeholders/departments]

## {terms['visualization_suggestions']}
*   **Executive Dashboard Components:**
    *   Revenue trend line chart with deal count overlay
    *   Service category revenue pie chart with {context_company_name} capability heatmap
    *   White space opportunity bubble chart (size=opportunity, color=priority)
    *   Quarterly closure pattern analysis
    *   Lead time vs. deal size scatter plot
    *   Competitive landscape radar chart

*   **Operational Analytics:**
    *   Deal pipeline funnel analysis
    *   Win/loss rate by category
    *   Account penetration depth metrics

## {terms['risks_mitigation']}
*   **Strategic Risk Assessment:**

    | Risk Category | Specific Risk | Probability | Impact | Mitigation Strategy | Owner |
    |---------------|---------------|-------------|--------|-------------------|-------|
    | Competitive | [Specific threat] | [High/Med/Low] | [High/Med/Low] | [Specific actions] | [Team/Role] |
    | Client Relationship | [Specific threat] | [High/Med/Low] | [High/Med/Low] | [Specific actions] | [Team/Role] |
    | Technology | [Specific threat] | [High/Med/Low] | [High/Med/Low] | [Specific actions] | [Team/Role] |

*   **Mitigation Action Plan:**
    *   Immediate Actions (0-3 months)
    *   Medium-term Actions (3-12 months)
    *   Long-term Strategic Actions (12+ months)

**Critical Processing Instructions:**

### Data Extraction & Validation
1. **JSON Structure Validation:** 
   - Verify presence of 'accounts' and 'opportunities' arrays
   - Handle malformed JSON gracefully with specific error messages
   - Cross-reference AccountId relationships between arrays

2. **Company Matching:**
   - Match `company_name` exactly with 'Name' or 'CT_NameAbbreviation__c' in accounts array
   - If no exact match: return {terms['error_not_found']}
   - Extract all opportunities linked to matched account via AccountId

3. **Data Quality Controls:**
   - Won Deal Filtering: Include only `IsWon == true` AND `Amount > 0` AND valid `CloseDate`
   - Handle null/empty values: Exclude from calculations but document in limitations
   - Currency validation: Ensure Amount fields are numeric and properly formatted
   - Date validation: Verify CloseDate and CreatedDate are valid date formats

### Analysis Processing Standards
4. **Tag Field Processing:**
   - Parse comma/semicolon-separated strings into distinct items
   - Clean whitespace and normalize casing
   - Handle special characters and encoding issues
   - Remove empty or placeholder values ("N/A", "None", etc.)

5. **Categorization Methodology:**
   - Primary: Use structured opportunity fields (Type, LeadSource, custom tags)
   - Secondary: Parse opportunity Name for service/product keywords
   - Tertiary: Infer from Amount ranges and CloseDate patterns
   - Document categorization logic used for each analysis

6. **Financial Calculations:**
   - Currency: Format all amounts in {terms['unit_currency']} with thousands separators
   - Percentages: Round to 1 decimal place, ensure totals equal 100%
   - Averages: Exclude null/zero values, show sample size for context
   - Growth rates: Use consistent baseline periods, handle negative growth appropriately

### Table Generation Requirements
7. **Table Standards:**
   - Use markdown format with proper column alignment
   - Include units in headers: ({terms['unit_currency']}, {terms['unit_deals']}, {terms['unit_days']})
   - Sort by most significant metric (usually Total Revenue)
   - Include "Other/Miscellaneous" category for small items
   - Show both absolute and percentage values where applicable

8. **Data Visualization Specifications:**
   - Priority indicators: 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
   - Trend indicators: ↗️ Growing / ↘️ Declining / ↔️ Stable
   - Confidence levels: High (>10 deals) / Medium (3-10 deals) / Low (<3 deals)

### Strategic Analysis Framework
9. **{context_company_name} Capability Mapping:**
   - Map each identified opportunity to specific {context_company_name} service offerings
   - Assess capability gaps and partnership requirements
   - Include competitive differentiation factors
   - Provide implementation difficulty assessment

10. **White Space Identification:**
    - Cross-reference account profile tags with actual won deal categories
    - Identify service gaps where client shows interest but limited {context_company_name} presence
    - Prioritize based on deal size potential and strategic alignment
    - Include market timing considerations

### Output Quality Controls
11. **Consistency Checks:**
    - Verify all monetary totals sum correctly across tables
    - Ensure percentage calculations are accurate
    - Cross-check deal counts between different analysis sections
    - Validate that recommendations align with data findings

12. **Limitation Documentation:**
    - State data quality issues encountered
    - Note any assumptions made in categorization
    - Highlight areas where sample sizes are too small for reliable analysis
    - Include confidence intervals for key metrics where appropriate

### Error Handling Protocols
13. **Insufficient Data Scenarios:**
    - If no won deals: Proceed with account profile analysis only
    - If limited data: Use available data but clearly state limitations
    - If calculation errors: Show "N/A" rather than incorrect values
    - If company not found: Return standardized error message

14. **Final Validation:**
    - Review all tables for completeness and accuracy
    - Ensure strategic recommendations are supported by data
    - Verify language consistency throughout ({language})
    - Check that all {context_company_name} references are appropriate

**Output Requirements:**
- **Language:** {language}
- **Format:** Professional business analysis report with structured sections, tables, and actionable recommendations
- **Perspective:** Internal {context_company_name} strategic analysis
- **Timeframe:** Include both tactical (6-month) and strategic (1-3 year) recommendations
- **Deliverable:** Executive-ready analysis with clear next steps and success metrics

{formatted_completion_template}
{formatted_final_review}
{formatted_base_formatting}
"""
    return prompt
