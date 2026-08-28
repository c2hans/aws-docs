---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.html
---

# DescribeIamInstanceProfileAssociations
<a name="API_DescribeIamInstanceProfileAssociations"></a>

Describes your IAM instance profile associations.

## Request Parameters
<a name="API_DescribeIamInstanceProfileAssociations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId.N**
The IAM instance profile associations.
Type: Array of strings
Required: No

 **Filter.N**
The filters.
+  `instance-id` - The ID of the instance.
+  `state` - The state of the association (`associating` \| `associated` \| `disassociating`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeIamInstanceProfileAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **iamInstanceProfileAssociationSet**
Information about the IAM instance profile associations.
Type: Array of [IamInstanceProfileAssociation](API_IamInstanceProfileAssociation.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeIamInstanceProfileAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeIamInstanceProfileAssociations_Examples"></a>

### Example
<a name="API_DescribeIamInstanceProfileAssociations_Example_1"></a>

This example describes all of your IAM instance profile associations.

#### Sample Request
<a name="API_DescribeIamInstanceProfileAssociations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeIamInstanceProfileAssociations
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeIamInstanceProfileAssociations_Example_1_Response"></a>

```
<DescribeIamInstanceProfileAssociationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>84c2d2a6-12dc-491f-a9ee-example</requestId>
    <iamInstanceProfileAssociations>
        <item>
            <associationId>iip-assoc-08049da59357d598c</associationId>
            <iamInstanceProfile>
                <arn>arn:aws:iam::123456789012:instance-profile/AdminProfile</arn>
                <id>AIPAJEDNCAA64SSD265D6</id>
            </iamInstanceProfile>
            <instanceId>i-1234567890abcdef0</instanceId>
            <state>associated</state>
        </item>
    </iamInstanceProfileAssociations>
</DescribeIamInstanceProfileAssociationsResponse>
```

## See Also
<a name="API_DescribeIamInstanceProfileAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeIamInstanceProfileAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
