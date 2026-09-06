---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ServiceLastAccessed.html
---

# ServiceLastAccessed
<a name="API_ServiceLastAccessed"></a>

Contains details about the most recent attempt to access the service.

This data type is used as a response element in the [GetServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetails.html) operation.

## Contents
<a name="API_ServiceLastAccessed_Contents"></a>

 ** ServiceName **
The name of the service in which access was attempted.
Type: String
Required: Yes

 ** ServiceNamespace **
The namespace of the service in which access was attempted.
To learn the service namespace of a service, see [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the *Service Authorization Reference*. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, `(service prefix: a4b)`. For more information about service namespaces, see [AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]*`
Required: Yes

 ** LastAuthenticated **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when an authenticated entity most recently attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: Timestamp
Required: No

 ** LastAuthenticatedEntity **
The ARN of the authenticated entity (user or role) that last attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** LastAuthenticatedRegion **
The Region from which the authenticated entity (user or role) last attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no IAM entities attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: String
Required: No

 ** TotalAuthenticatedEntities **
The total number of authenticated principals (root user, IAM users, or IAM roles) that have attempted to access the service.
This field is null if no principals attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: Integer
Required: No

 ** TrackedActionsLastAccessed.member.N **
An object that contains details about the most recent attempt to access a tracked action within the service.
This field is null if there no tracked actions or if the principal did not use the tracked actions within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period). This field is also null if the report was generated at the service level and not the action level. For more information, see the `Granularity` field in [GenerateServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateServiceLastAccessedDetails.html).
Type: Array of [TrackedActionLastAccessed](API_TrackedActionLastAccessed.md) objects
Required: No

## See Also
<a name="API_ServiceLastAccessed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ServiceLastAccessed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ServiceLastAccessed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ServiceLastAccessed)
