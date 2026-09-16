---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteSubnetGroup.html
---

# DeleteSubnetGroup
<a name="API_dax_DeleteSubnetGroup"></a>

Deletes a subnet group.

**Note**
You cannot delete a subnet group if it is associated with any DAX clusters.

## Request Syntax
<a name="API_dax_DeleteSubnetGroup_RequestSyntax"></a>

```
{
   "SubnetGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_dax_DeleteSubnetGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [SubnetGroupName](#API_dax_DeleteSubnetGroup_RequestSyntax) **   <a name="DDB-dax_DeleteSubnetGroup-request-SubnetGroupName"></a>
The name of the subnet group to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_dax_DeleteSubnetGroup_ResponseSyntax"></a>

```
{
   "DeletionMessage": "string"
}
```

## Response Elements
<a name="API_dax_DeleteSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionMessage](#API_dax_DeleteSubnetGroup_ResponseSyntax) **   <a name="DDB-dax_DeleteSubnetGroup-response-DeletionMessage"></a>
A user-specified message for this action (i.e., a reason for deleting the subnet group).
Type: String

## Errors
<a name="API_dax_DeleteSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** SubnetGroupInUseFault **
The specified subnet group is currently in use.
HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **
The requested subnet group name does not refer to an existing subnet group.
HTTP Status Code: 400

## See Also
<a name="API_dax_DeleteSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DeleteSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DeleteSubnetGroup)
