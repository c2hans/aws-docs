---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/licensing.html
---

# SAP licensing
<a name="licensing"></a>

The use of SAP software is subject to SAP’s terms. You are responsible for complying with SAP licensing terms, including software distribution and indirect licensing conditions. Any information provided is not legal advice, and should not be relied upon for licensing compliance purposes. If you have questions about your licensing or rights to SAP software, consult your legal team, SAP, and/or your SAP reseller.

**Question** : Will SDK for SAP ABAP usage affect my SAP license?

**Answer** : AWS SDK for SAP ABAP enables you to consume AWS services with your own ABAP code. It is used in integration scenarios between an SAP system and AWS services. Any scenario where data from the SAP system is sent to a third-party (non-SAP) system, or created by that system, may have implications for indirect licensing. SAP has multiple approaches for defining indirect access, such as user-based calculations and outcome-based calculations. The methodology to define indirect access depends on your contract with SAP. You must be aware of the guidance provided in your contract with SAP, and you can further discuss this with SAP or their reseller.

In 2018, SAP released two documents – *Indirect Access Guide for SAP Installed Base Customers* and *SAP ERP Pricing for Digital Age - Addressing Indirect/Digital Access*. These documents can be found on SAP websites, and are examples of indirect licensing approaches. However, these documents do not reflect your particular agreement with SAP.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
