---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResourceDrift.html
---

# ResourceDrift
<a name="API_ResourceDrift"></a>

Indicates the resources that have drifted in the current application version.

## Contents
<a name="API_ResourceDrift_Contents"></a>

 ** appArn **   <a name="resiliencehub-Type-ResourceDrift-appArn"></a>
Amazon Resource Name (ARN) of the application whose resources have drifted. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** appVersion **   <a name="resiliencehub-Type-ResourceDrift-appVersion"></a>
Version of the application whose resources have drifted.
Type: String
Pattern: `\S{1,50}`
Required: No

 ** diffType **   <a name="resiliencehub-Type-ResourceDrift-diffType"></a>
Indicates if the resource was added or removed.
Type: String
Valid Values: `NotEqual | Added | Removed`
Required: No

 ** referenceId **   <a name="resiliencehub-Type-ResourceDrift-referenceId"></a>
Reference identifier of the resource drift.
Type: String
Pattern: `\S{1,255}`
Required: No

 ** resourceIdentifier **   <a name="resiliencehub-Type-ResourceDrift-resourceIdentifier"></a>
Identifier of the drifted resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: No

## See Also
<a name="API_ResourceDrift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ResourceDrift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ResourceDrift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ResourceDrift)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
