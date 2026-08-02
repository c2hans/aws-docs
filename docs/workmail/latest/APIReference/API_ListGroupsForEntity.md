---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupsForEntity.html
---

# ListGroupsForEntity
<a name="API_ListGroupsForEntity"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Returns all the groups to which an entity belongs.

## Request Syntax
<a name="API_ListGroupsForEntity_RequestSyntax"></a>

```
{
   "EntityId": "{{string}}",
   "Filters": {
      "GroupNamePrefix": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGroupsForEntity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EntityId](#API_ListGroupsForEntity_RequestSyntax) **   <a name="workmail-ListGroupsForEntity-request-EntityId"></a>
The identifier for the entity.
The entity ID can accept *UserId or GroupID*, *Username or Groupname*, or *email*.
+ Entity ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: entity@domain.tld
+ Entity name: entity
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

 ** [Filters](#API_ListGroupsForEntity_RequestSyntax) **   <a name="workmail-ListGroupsForEntity-request-Filters"></a>
Limit the search results based on the filter criteria.
Type: [ListGroupsForEntityFilters](API_ListGroupsForEntityFilters.md) object
Required: No

 ** [MaxResults](#API_ListGroupsForEntity_RequestSyntax) **   <a name="workmail-ListGroupsForEntity-request-MaxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListGroupsForEntity_RequestSyntax) **   <a name="workmail-ListGroupsForEntity-request-NextToken"></a>
The token to use to retrieve the next page of results. The first call does not contain any tokens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`
Required: No

 ** [OrganizationId](#API_ListGroupsForEntity_RequestSyntax) **   <a name="workmail-ListGroupsForEntity-request-OrganizationId"></a>
The identifier for the organization under which the entity exists.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_ListGroupsForEntity_ResponseSyntax"></a>

```
{
   "Groups": [
      {
         "GroupId": "string",
         "GroupName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGroupsForEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Groups](#API_ListGroupsForEntity_ResponseSyntax) **   <a name="workmail-ListGroupsForEntity-response-Groups"></a>
The overview of groups in an organization.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects

 ** [NextToken](#API_ListGroupsForEntity_ResponseSyntax) **   <a name="workmail-ListGroupsForEntity-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`

## Errors
<a name="API_ListGroupsForEntity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** EntityStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You are performing an operation on a user, group, or resource that isn't in the expected state, such as trying to delete an active user.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

## See Also
<a name="API_ListGroupsForEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/ListGroupsForEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListGroupsForEntity)
