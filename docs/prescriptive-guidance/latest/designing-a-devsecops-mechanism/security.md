---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/security.html
---

# Security
<a name="security"></a>

A central code inspection, compilation, and reporting mechanism can provide great security benefits and reduce time to market by freeing application developers from writing this task.

Consider how your organization reports security vulnerabilities and code inspection results. For example, the following approaches to reporting are typical:
+ Pipeline stoppage
+ Email messages and a dashboard

If you choose to stop merges and deployments because of security scan results, you must provide two solutions:
+ A clear mechanism to communicate and resolve the issue.
+ A responsive central scan standard that can keep up with changing IAC standards.

Imagine a scenario where your central security scan mistakenly requires an encryption key parameter to be in a specific format for the creation of a resource. (An Amazon Resource Name (ARN) string is an example of a resource.) However, the application team needs to create dozens of these resources and they use a `for `loop in the IaC to pass in the key ARN. Now, the security requirement is met, but the scan tool doesn't reflect good coding practices accurately. This approach can cause delays in delivery and frustrate developers.
