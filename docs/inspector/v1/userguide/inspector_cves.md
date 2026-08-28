---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_cves.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Common vulnerabilities and exposures
<a name="inspector_cves"></a>

The rules in this package help verify whether the EC2 instances in your assessment targets are exposed to common vulnerabilities and exposures (CVEs). Attacks can exploit unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of your service or data. The CVE system provides a reference method for publicly known information security vulnerabilities and exposures. For more information, see [ https://cve.mitre.org/](https://cve.mitre.org/).

If a particular CVE appears in a *finding* that is produced by an Amazon Inspector Classic assessment, you can search [https://cve.mitre.org/](https://cve.mitre.org/) for the ID of the CVE (for example, **CVE-2009-0021**). The search results can provide detailed information about this CVE, its severity, and how to mitigate it.

For the Common Vulnerabilities & Exploits (CVE) rules package, Amazon Inspector has mapped the provided CVSS Base Scoring and ALAS Severity levels provided:

|
|
| **Amazon Inspector Severity ** | **CVSS Base Score ** | **ALAS Severity (if CVSS not scored)** |
| --- |--- |--- |
| High | >= 5  | Critical or Important |
| Medium | < 5 and >= 2.1  | Medium |
| Low | < 2.1 and >= 0.8  | Low |
| Informational | < 0.8 | N/A |

The rules included in this package help you assess whether your EC2 instances are exposed to the CVEs in the following regional lists:
+ [US East (N. Virginia)](https://s3.us-east-1.amazonaws.com/rules-engine.us-east-1/CVEList.txt)
+ [US East (Ohio)](https://s3.us-east-2.amazonaws.com/rules-engine.us-east-2/CVEList.txt)
+ [US West (N. California)](https://s3.us-west-1.amazonaws.com/rules-engine.us-west-1/CVEList.txt)
+ [US West (Oregon)](https://s3.us-west-2.amazonaws.com/rules-engine.us-west-2/CVEList.txt)
+ [EU (Ireland)](https://s3.eu-west-1.amazonaws.com/rules-engine.eu-west-1/CVEList.txt)
+ [EU (Frankfurt)](https://s3.eu-central-1.amazonaws.com/rules-engine.eu-central-1/CVEList.txt)
+ [EU (London)](https://s3.eu-west-2.amazonaws.com/rules-engine.eu-west-2/CVEList.txt)
+ [EU (Stockholm)](https://s3.eu-north-1.amazonaws.com/rules-engine.eu-north-1/CVEList.txt)
+ [Asia Pacific (Tokyo)](https://s3.ap-northeast-1.amazonaws.com/rules-engine.ap-northeast-1/CVEList.txt)
+ [Asia Pacific (Seoul)](https://s3.ap-northeast-2.amazonaws.com/rules-engine.ap-northeast-2/CVEList.txt)
+ [Asia Pacific (Mumbai)](https://s3.ap-south-1.amazonaws.com/rules-engine.ap-south-1/CVEList.txt)
+ [Asia Pacific (Sydney)](https://s3.ap-southeast-2.amazonaws.com/rules-engine.ap-southeast-2/CVEList.txt)
+ [AWS GovCloud West (US)](https://s3.us-gov-west-1.amazonaws.com/rules-engine.us-gov-west-1/CVEList.txt)
+ [AWS GovCloud East (US)](https://s3.us-gov-east-1.amazonaws.com/rules-engine.us-gov-east-1/CVEList.txt)

The CVE rules package is updated regularly; this list includes the CVEs that are included in assessments runs that occur at the same time that this list is retrieved.

For more information, see [Amazon Inspector Classic rules packages for supported operating systems](inspector_rule-packages_across_os.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
