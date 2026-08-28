---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTags.html
---

# DescribeTags
<a name="API_DescribeTags"></a>

Describes the specified tags for your EC2 resources.

For more information about tags, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Important**
We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeTags_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `key` - The tag key.
+  `resource-id` - The ID of the resource.
+  `resource-type` - The resource type. For a list of possible values, see [TagSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TagSpecification.html).
+  `tag`:<key> - The key/value combination of the tag. For example, specify "tag:Owner" for the filter name and "TeamA" for the filter value to find resources with the tag "Owner=TeamA".
+  `value` - The tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. This value can be between 5 and 1000. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeTags_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **tagSet**
The tags.
Type: Array of [TagDescription](API_TagDescription.md) objects

## Errors
<a name="API_DescribeTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeTags_Examples"></a>

### Example
<a name="API_DescribeTags_Example_1"></a>

This example describes all the tags in your account.

#### Sample Request
<a name="API_DescribeTags_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTags
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_1_Response"></a>

```
<DescribeTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/"/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <tagSet>
      <item>
         <resourceId>ami-1a2b3c4d</resourceId>
         <resourceType>image</resourceType>
         <key>webserver</key>
         <value/>
      </item>
       <item>
         <resourceId>ami-1a2b3c4d</resourceId>
         <resourceType>image</resourceType>
         <key>stack</key>
         <value>Production</value>
      </item>
      <item>
         <resourceId>i-1234567890abcdef0</resourceId>
         <resourceType>instance</resourceType>
         <key>webserver</key>
         <value/>
      </item>
       <item>
         <resourceId>i-1234567890abcdef0</resourceId>
         <resourceType>instance</resourceType>
         <key>stack</key>
         <value>Production</value>
      </item>
      <item>
         <resourceId>i-0598c7d356eba48d7</resourceId>
         <resourceType>instance</resourceType>
         <key>database_server</key>
         <value/>
      </item>
       <item>
         <resourceId>i-0598c7d356eba48d7</resourceId>
         <resourceType>instance</resourceType>
         <key>stack</key>
         <value>Test</value>
      </item>
    </tagSet>
</DescribeTagsResponse>
```

### Example
<a name="API_DescribeTags_Example_2"></a>

This example describes only the tags for the AMI with ID ami-1a2b3c4d.

#### Sample Request
<a name="API_DescribeTags_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTags
&Filter.1.Name=resource-id
&Filter.1.Value.1=ami-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_2_Response"></a>

```
<DescribeTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/"/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <tagSet>
      <item>
         <resourceId>ami-1a2b3c4d</resourceId>
         <resourceType>image</resourceType>
         <key>webserver</key>
         <value/>
      </item>
      <item>
         <resourceId>ami-1a2b3c4d</resourceId>
         <resourceType>image</resourceType>
         <key>stack</key>
         <value>Production</value>
      </item>
    </tagSet>
</DescribeTagsResponse>
```

### Example
<a name="API_DescribeTags_Example_3"></a>

This example describes the tags for all your instances.

#### Sample Request
<a name="API_DescribeTags_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTags
&Filter.1.Name=resource-type
&Filter.1.Value.1=instance
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_3_Response"></a>

```
<DescribeTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/"/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <tagSet>
       <item>
         <resourceId>i-0598c7d356eba48d7</resourceId>
         <resourceType>instance</resourceType>
         <key>webserver</key>
         <value/>
      </item>
       <item>
         <resourceId>i-0598c7d356eba48d7</resourceId>
         <resourceType>instance</resourceType>
         <key>stack</key>
         <value>Production</value>
      </item>
      <item>
         <resourceId>i-1234567890abcdef0</resourceId>
         <resourceType>instance</resourceType>
         <key>database_server</key>
         <value/>
      </item>
       <item>
         <resourceId>i-1234567890abcdef0</resourceId>
         <resourceType>instance</resourceType>
         <key>stack</key>
         <value>Test</value>
      </item>
    </tagSet>
</DescribeTagsResponse>
```

### Example
<a name="API_DescribeTags_Example_4"></a>

This example describes the tags for all your instances tagged with the key *webserver*. You can use wildcards with filters, so you could specify the value as `?ebserver` to find tags with the key *webserver* or *Webserver*.

#### Sample Request
<a name="API_DescribeTags_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTags
&Filter.1.Name=key
&Filter.1.Value.1=webserver
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_4_Response"></a>

```
<DescribeTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/"/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <tagSet>
       <item>
         <resourceId>i-1234567890abcdef0</resourceId>
         <resourceType>instance</resourceType>
         <key>webserver</key>
         <value/>
      </item>
    </tagSet>
</DescribeTagsResponse>
```

### Example
<a name="API_DescribeTags_Example_5"></a>

This example describes the tags for all your instances tagged with either stack=Test or stack=Production.

#### Sample Request
<a name="API_DescribeTags_Example_5_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTags
&Filter.1.Name=resource-type
&Filter.1.Value.1=instance
&Filter.2.Name=key
&Filter.2.Value.1=stack
&Filter.3.Name=value
&Filter.3.Value.1=Test
&Filter.3.Value.2=Production
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_5_Response"></a>

```
<DescribeTagsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/"/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <tagSet>
       <item>
         <resourceId>i-1234567890abcdef0</resourceId>
         <resourceType>instance</resourceType>
         <key>stack</key>
         <value>Production</value>
      </item>
       <item>
         <resourceId>i-0598c7d356eba48d7</resourceId>
         <resourceType>instance</resourceType>
         <key>stack</key>
         <value>Test</value>
      </item>
    </tagSet>
</DescribeTagsResponse>
```

### Example
<a name="API_DescribeTags_Example_6"></a>

This example describes the tags for all your instances tagged with Purpose=[empty string].

#### Sample Request
<a name="API_DescribeTags_Example_6_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTags
&Filter.1.Name=resource-type
&Filter.1.Value.1=instance
&Filter.2.Name=key
&Filter.2.Value.1=Purpose
&Filter.3.Name=value
&Filter.3.Value.1=
&AUTHPARAMS
```

## See Also
<a name="API_DescribeTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
