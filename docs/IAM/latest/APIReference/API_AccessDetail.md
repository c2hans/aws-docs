---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessDetail.html
---

# AccessDetail
<a name="API_AccessDetail"></a>

An object that contains details about when a principal in the reported AWS Organizations entity last attempted to access an AWS service. A principal can be an IAM user, an IAM role, or the AWS account root user within the reported Organizations entity.

This data type is a response element in the [GetOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html) operation.

## Contents
<a name="API_AccessDetail_Contents"></a>

 ** ServiceName **
The name of the service in which access was attempted.
Type: String
Required: Yes

 ** ServiceNamespace **
The namespace of the service in which access was attempted.
To learn the service namespace of a service, see [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the *Service Authorization Reference*. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, `(service prefix: a4b)`. For more information about service namespaces, see [AWS service namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]*`
Required: Yes

 ** EntityPath **
The path of the Organizations entity (root, organizational unit, or account) from which an authenticated principal last attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no principals (IAM users, IAM roles, or root user) in the reported Organizations entity attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: String
Length Constraints: Minimum length of 19. Maximum length of 427.
Pattern: `^o-[0-9a-z]{10,32}\/r-[0-9a-z]{4,32}[0-9a-z-\/]*`
Required: No

 ** LastAuthenticatedTime **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when an authenticated principal most recently attempted to access the service. AWS does not report unauthenticated requests.
This field is null if no principals in the reported Organizations entity attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: Timestamp
Required: No

 ** Region **
The Region where the last service access attempt occurred.
This field is null if no principals in the reported Organizations entity attempted to access the service within the [tracking period](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period).
Type: String
Required: No

 ** TotalAuthenticatedEntities **
The number of accounts with authenticated principals (root user, IAM users, and IAM roles) that attempted to access the service in the tracking period.
Type: Integer
Required: No

## See Also
<a name="API_AccessDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AccessDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AccessDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AccessDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
