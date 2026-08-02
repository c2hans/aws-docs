---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/llm-prompt-engineering-best-practices/comparisons.html
---

# Comparing prompt templates
<a name="comparisons"></a>

The following comparison is performed between two prompt templates:
+ A basic RAG prompt template with a financial analyst persona
+ A proposed template that applies the guardrails discussed in the [previous section](best-practices.md)

These templates are compared across questions that pertain to the common attack categories. The comparison was performed on the [EDGAR dataset](https://www.sec.gov/os/accessing-edgar-data), where the LLM is instructed to answer questions about three companies (anonymized for this article as *Company-1*, *Company-2*, and *Company-3*) from a financial analyst's perspective by using public financial documents.
