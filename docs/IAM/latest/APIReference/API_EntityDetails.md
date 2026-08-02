---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_EntityDetails.html
---

# EntityDetails
<a name="API_EntityDetails"></a>

An object that contains details about when the IAM entities (users or roles) were last used in an attempt to access the specified AWS service.

This data type is a response element in the [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetailsWithEntities.html) operation.

## Contents
<a name="API_EntityDetails_Contents"></a>

 ** EntityInfo **
The `EntityInfo` object that contains details about the entity (user or role).
Type: [EntityInfo](API_EntityInfo.md) object
Required: Yes

 ** LastAuthenticated **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the authenticated entity last attempted to access AWS. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: Timestamp
Required: No

## See Also
<a name="API_EntityDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/EntityDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/EntityDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/EntityDetails)
