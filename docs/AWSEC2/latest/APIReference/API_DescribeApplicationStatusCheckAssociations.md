---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeApplicationStatusCheckAssociations.html
---

# DescribeApplicationStatusCheckAssociations
<a name="API_DescribeApplicationStatusCheckAssociations"></a>

Describes the associations for one or more application status checks. For more information, see [Application status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-application-status-checks.html). To avoid timeouts and retrieve complete results, use the pagination parameters.

**Note**
The order of the elements in the response, including those within nested structures, might vary.

## Request Parameters
<a name="API_DescribeApplicationStatusCheckAssociations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ApplicationStatusCheckId.N**
The IDs of the application status checks for which to describe associations.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters to use to limit the results.
+  `association-type` – The type of association. Valid values: `tag` and `instance-id`.
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
<a name="API_DescribeApplicationStatusCheckAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **associationSet**
The associations for the specified application status checks.
Type: Array of [ApplicationStatusCheckAssociationObject](API_ApplicationStatusCheckAssociationObject.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **tagSet**
The tags associated with the application status checks.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_DescribeApplicationStatusCheckAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeApplicationStatusCheckAssociations_Examples"></a>

### To describe application status check associations
<a name="API_DescribeApplicationStatusCheckAssociations_Example_1"></a>

The following example describes the associations for the specified application status check.

#### Sample Request
<a name="API_DescribeApplicationStatusCheckAssociations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeApplicationStatusCheckAssociations
&ApplicationStatusCheckId.1=asc-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeApplicationStatusCheckAssociations_Example_1_Response"></a>

```
<DescribeApplicationStatusCheckAssociationsResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <associationSet>
        <item>
            <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
            <associationType>instance-id</associationType>
            <value>i-0123456789abcdef0</value>
        </item>
    </associationSet>
</DescribeApplicationStatusCheckAssociationsResult>
```

## See Also
<a name="API_DescribeApplicationStatusCheckAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeApplicationStatusCheckAssociations)
