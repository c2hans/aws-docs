---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksSecret.html
---

# EksSecret
<a name="API_EksSecret"></a>

Specifies the configuration of a Kubernetes `secret` volume. For more information, see [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret) in the *Kubernetes documentation*.

## Contents
<a name="API_EksSecret_Contents"></a>

 ** secretName **   <a name="Batch-Type-EksSecret-secretName"></a>
The name of the secret. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation*.
Type: String
Required: Yes

 ** optional **   <a name="Batch-Type-EksSecret-optional"></a>
Specifies whether the secret or the secret's keys must be defined.
Type: Boolean
Required: No

## See Also
<a name="API_EksSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksSecret)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
