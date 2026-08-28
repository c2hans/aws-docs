---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RelatedResource.html
---

# RelatedResource
<a name="API_RelatedResource"></a>

Information about a related resource.

## Contents
<a name="API_RelatedResource_Contents"></a>

 ** additionalInfo **   <a name="iot-Type-RelatedResource-additionalInfo"></a>
Other information about the resource.
Type: String to string map
Required: No

 ** resourceIdentifier **   <a name="iot-Type-RelatedResource-resourceIdentifier"></a>
Information that identifies the resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: No

 ** resourceType **   <a name="iot-Type-RelatedResource-resourceType"></a>
The type of resource.
Type: String
Valid Values: `DEVICE_CERTIFICATE | CA_CERTIFICATE | IOT_POLICY | COGNITO_IDENTITY_POOL | CLIENT_ID | ACCOUNT_SETTINGS | ROLE_ALIAS | IAM_ROLE | ISSUER_CERTIFICATE`
Required: No

## See Also
<a name="API_RelatedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RelatedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RelatedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RelatedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
