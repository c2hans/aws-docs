---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/naive-modulo-mapping-or-fixed-partition-number.html
---

# Naïve modulo mapping or fixed partition number
<a name="naive-modulo-mapping-or-fixed-partition-number"></a>

 Naïve modulo mapping uses modular arithmetic to map keys to cells, typically on a cryptographic hash of the key. This scheme has an effective zero peak-to-average ratio (very even distribution) and requires minimal state (just the count of cells). But it suffers from high churn (cell reassignment) when adding or removing cells.

 Advantages:
+  Simple to implement.
+  Avoids hot cells.

 Disadvantages:
+  Changing the number of cells requires the rebalance of all cells and their customers and tenants.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
