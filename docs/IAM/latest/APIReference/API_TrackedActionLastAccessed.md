---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_TrackedActionLastAccessed.html
---

# TrackedActionLastAccessed
<a name="API_TrackedActionLastAccessed"></a>

Contains details about the most recent attempt to access an action within the service.

This data type is used as a response element in the [GetServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetails.html) operation.

## Contents
<a name="API_TrackedActionLastAccessed_Contents"></a>

 ** ActionName **
The name of the tracked action to which access was attempted. Tracked actions are actions that report activity to IAM.
Type: String
Required: No

 ** LastAccessedEntity **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** LastAccessedRegion **
The Region from which the authenticated entity (user or role) last attempted to access the tracked action. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: String
Required: No

 ** LastAccessedTime **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when an authenticated entity most recently attempted to access the tracked service. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: Timestamp
Required: No

## See Also
<a name="API_TrackedActionLastAccessed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/TrackedActionLastAccessed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/TrackedActionLastAccessed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/TrackedActionLastAccessed)
