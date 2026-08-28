---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/managing-data-access-for-data-science-teams.html
---

# Managing data access for data science teams
<a name="managing-data-access-for-data-science-teams"></a>

 Data science teams need access to real-world data to do their jobs. Deidentification of production data is one approach that you can use to reduce the risk of improper data handling. However, deidentification can be challenging. The United States and other countries have differing definitions of PII. For example, in the EU, if a person can be re-identified, then the GDPR doesn't recognize the data as deidentified.

 Synthetic data is another approach, but this might have lower fidelity. The debate is ongoing on whether we will run into a peak data scenario that impacts effective scaling of generative AI. However, new approaches to generating synthetic data are increasingly showing efficacy for generative AI applications. In some cases, using generative AI to create synthetic data risks biasing the output of synthetic data based on the bias of the data the generative AI model was trained on.

 One approach is to use auditing. Auditing has been successfully used in healthcare to protect protected health information (PHI). Care teams often need access to sensitive data to do their jobs. Preventing access can have safety ramifications, but still needs to be balanced with security. A similar approach can be used to maintain appropriate use of data. Automation can be applied to audit logs that can identify anomalous behavior. This has been successful in large health systems where it has identified care team members who were accessing data they should not have.

 Finally, keeping data contained in the cloud where the security team maintains the environment is a way to protect against data leaks. After data ends up on a local workstation, controlling access to it becomes almost impossible, even with data loss prevention tools. When appropriate controls are applied, the cloud can adhere to the most stringent security requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
