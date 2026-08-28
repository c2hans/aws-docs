---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec09-bp01.html
---

# GAMESEC09-BP01 Integrate tooling and automation to reduce the mean time of security reviews
<a name="gamesec09-bp01"></a>

 To identify security vulnerabilities, organizations can use a variety of different tools and services like Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST). SAST is a way to review the source code and determine security vulnerability. DAST is a black box way of testing your code which tests your applications without looking at the source code.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-36"></a>

 Another tool that organizations can use is Software Composition Analysis (SCA), which assesses the security of your third-party or open source dependencies. For a more manual approach, secure code reviews can be implemented throughout the pipeline.

 **Customer example**

 AnyCompany Games uses SAST tools to automatically flag potential security flaws during the development process. They also use DAST tools to simulate threats against running game builds to validate that security controls are working as intended. Additionally, AnyCompany Games integrates dependency scanning tools into their development process to automatically identify known vulnerabilities in third-party libraries and game engines.

### Implementation steps
<a name="implementation-steps-35"></a>
+  Use Amazon CodeGuru as a SAST tool.
+  Use open-source tools like OWASP Dependency Check, SonarQube, or OWASPZap.

### Resources
<a name="resources-4"></a>
+  [Security for Developers](https://catalog.us-east-1.prod.workshops.aws/workshops/66275888-6bab-4872-8c6e-ed2fe132a362/en-US)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
