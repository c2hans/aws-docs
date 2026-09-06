---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_NonCompliantResource.html
---

# NonCompliantResource
<a name="API_NonCompliantResource"></a>

Information about the resource that was noncompliant with the audit check.

## Contents
<a name="API_NonCompliantResource_Contents"></a>

 ** additionalInfo **   <a name="iot-Type-NonCompliantResource-additionalInfo"></a>
Other information about the noncompliant resource.
Type: String to string map
Required: No

 ** resourceIdentifier **   <a name="iot-Type-NonCompliantResource-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: No

 ** resourceType **   <a name="iot-Type-NonCompliantResource-resourceType"></a>
The type of the noncompliant resource.
Type: String
Valid Values: `DEVICE_CERTIFICATE | CA_CERTIFICATE | IOT_POLICY | COGNITO_IDENTITY_POOL | CLIENT_ID | ACCOUNT_SETTINGS | ROLE_ALIAS | IAM_ROLE | ISSUER_CERTIFICATE`
Required: No

## See Also
<a name="API_NonCompliantResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/NonCompliantResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/NonCompliantResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/NonCompliantResource)
