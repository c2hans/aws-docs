---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_ApiAssociation.html
---

# ApiAssociation
<a name="API_ApiAssociation"></a>

Describes an `ApiAssociation` object.

## Contents
<a name="API_ApiAssociation_Contents"></a>

 ** apiId **   <a name="appsync-Type-ApiAssociation-apiId"></a>
The API ID.
Type: String
Required: No

 ** associationStatus **   <a name="appsync-Type-ApiAssociation-associationStatus"></a>
Identifies the status of an association.
+  **PROCESSING**: The API association is being created. You cannot modify association requests during processing.
+  **SUCCESS**: The API association was successful. You can modify associations after success.
+  **FAILED**: The API association has failed. You can modify associations after failure.
Type: String
Valid Values: `PROCESSING | FAILED | SUCCESS`
Required: No

 ** deploymentDetail **   <a name="appsync-Type-ApiAssociation-deploymentDetail"></a>
Details about the last deployment status.
Type: String
Required: No

 ** domainName **   <a name="appsync-Type-ApiAssociation-domainName"></a>
The domain name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `^(\*[\w\d-]*\.)?([\w\d-]+\.)+[\w\d-]+$`
Required: No

## See Also
<a name="API_ApiAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/ApiAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/ApiAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/ApiAssociation)
