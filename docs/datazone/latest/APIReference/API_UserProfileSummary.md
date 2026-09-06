---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UserProfileSummary.html
---

# UserProfileSummary
<a name="API_UserProfileSummary"></a>

The details of the user profile.

## Contents
<a name="API_UserProfileSummary_Contents"></a>

 ** details **   <a name="datazone-Type-UserProfileSummary-details"></a>
The details of the user profile.
Type: [UserProfileDetails](API_UserProfileDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** domainId **   <a name="datazone-Type-UserProfileSummary-domainId"></a>
The ID of the Amazon DataZone domain of the user profile.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** id **   <a name="datazone-Type-UserProfileSummary-id"></a>
The ID of the user profile.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** status **   <a name="datazone-Type-UserProfileSummary-status"></a>
The status of the user profile.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED | ACTIVATED | DEACTIVATED`
Required: No

 ** type **   <a name="datazone-Type-UserProfileSummary-type"></a>
The type of the user profile.
Type: String
Valid Values: `IAM | SSO`
Required: No

## See Also
<a name="API_UserProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UserProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UserProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UserProfileSummary)
