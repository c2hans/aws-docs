---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/shared-repositories.html
---

# Shared repositories and contributions
<a name="shared-repositories"></a>

Some resource structures benefit from using a shared repository where contribution is expected from a wide audience. Common use cases involve the following access management issues:
+ Central AWS Identity and Access Management (IAM) role creation and management
+ Central repository creation and management
+ OpenID Connect (OIDC), Open Authorization (OAuth), and similar IAM protocols

To address these use cases, creating a workflow that uses change review is typically implemented.

The biggest challenge that an organization faces is not allowing or implementing these use cases. Trying to manage a central application construct in a distributed manner, such as repository creation in the organization, can result in access vulnerabilities and non-standardized processes.
