---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_mediastore_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# MediaStore examples using AWS CLI
<a name="cli_2_mediastore_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaStore.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-container`
<a name="mediastore_CreateContainer_cli_2_topic"></a>

The following code example shows how to use `create-container`.

**AWS CLI**
**To create a container**
The following `create-container` example creates a new, empty container.

```
aws mediastore create-container \
    --container-name {{ExampleContainer}}
```
Output:

```
{
    "Container": {
        "AccessLoggingEnabled": false,
        "CreationTime": 1563557265,
        "Name": "ExampleContainer",
        "Status": "CREATING",
        "ARN": "arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer"
    }
}
```
+  For API details, see [CreateContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/create-container.html) in *AWS CLI Command Reference*.

### `delete-container-policy`
<a name="mediastore_DeleteContainerPolicy_cli_2_topic"></a>

The following code example shows how to use `delete-container-policy`.

**AWS CLI**
**To delete a container policy**
The following `delete-container-policy` example deletes the policy that is assigned to the specified container. When the policy is deleted, AWS Elemental MediaStore automatically assigns the default policy to the container.

```
aws mediastore delete-container-policy \
    --container-name {{LiveEvents}}
```
This command produces no output.
+  For API details, see [DeleteContainerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container-policy.html) in *AWS CLI Command Reference*.

### `delete-container`
<a name="mediastore_DeleteContainer_cli_2_topic"></a>

The following code example shows how to use `delete-container`.

**AWS CLI**
**To delete a container**
The following `delete-container` example deletes the specified container. You can delete a container only if it has no objects.

```
aws mediastore delete-container \
    --container-name=ExampleLiveDemo
```
This command produces no output.
+  For API details, see [DeleteContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container.html) in *AWS CLI Command Reference*.

### `delete-cors-policy`
<a name="mediastore_DeleteCorsPolicy_cli_2_topic"></a>

The following code example shows how to use `delete-cors-policy`.

**AWS CLI**
**To delete a CORS policy**
The following `delete-cors-policy` example deletes the cross-origin resource sharing (CORS) policy that is assigned to the specified container.

```
aws mediastore delete-cors-policy \
    --container-name {{ExampleContainer}}
```
This command produces no output.
+  For API details, see [DeleteCorsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-cors-policy.html) in *AWS CLI Command Reference*.

### `delete-lifecycle-policy`
<a name="mediastore_DeleteLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `delete-lifecycle-policy`.

**AWS CLI**
**To delete an object lifecycle policy**
The following `delete-lifecycle-policy` example deletes the object lifecycle policy attached to the specified container. This change can take up to 20 minutes to take effect.

```
aws mediastore delete-lifecycle-policy \
    --container-name {{LiveEvents}}
```
This command produces no output.
+  For API details, see [DeleteLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-lifecycle-policy.html) in *AWS CLI Command Reference*.

### `describe-container`
<a name="mediastore_DescribeContainer_cli_2_topic"></a>

The following code example shows how to use `describe-container`.

**AWS CLI**
**To view the details of a container**
The following `describe-container` example displays the details of the specified container.

```
aws mediastore describe-container \
    --container-name {{ExampleContainer}}
```
Output:

```
{
    "Container": {
        "CreationTime": 1563558086,
        "AccessLoggingEnabled": false,
        "ARN": "arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer",
        "Status": "ACTIVE",
        "Name": "ExampleContainer",
        "Endpoint": "https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com"
    }
}
```
+  For API details, see [DescribeContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/describe-container.html) in *AWS CLI Command Reference*.

### `get-container-policy`
<a name="mediastore_GetContainerPolicy_cli_2_topic"></a>

The following code example shows how to use `get-container-policy`.

**AWS CLI**
**To view a container policy**
The following `get-container-policy` example displays the resource-based policy of the specified container.

```
aws mediastore get-container-policy \
    --container-name {{ExampleLiveDemo}}
```
Output:

```
{
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"PublicReadOverHttps\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:root\"},\"Action\":[\"mediastore:GetObject\",\"mediastore:DescribeObject\"],\"Resource\":\"arn:aws:mediastore:us-west-2:123456789012:container/ExampleLiveDemo/\",\"Condition\":{\"Bool\":{\"aws:SecureTransport\":\"true\"}}}]}"
}
```
+  For API details, see [GetContainerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-container-policy.html) in *AWS CLI Command Reference*.

### `get-cors-policy`
<a name="mediastore_GetCorsPolicy_cli_2_topic"></a>

The following code example shows how to use `get-cors-policy`.

**AWS CLI**
**To view a CORS policy**
The following `get-cors-policy` example displays the cross-origin resource sharing (CORS) policy that is assigned to the specified container.

```
aws mediastore get-cors-policy \
    --container-name {{ExampleContainer}}
```
Output:

```
{
    "CorsPolicy": [
        {
            "AllowedMethods": [
                "GET",
                "HEAD"
            ],
            "MaxAgeSeconds": 3000,
            "AllowedOrigins": [
                ""
            ],
            "AllowedHeaders": [
                ""
            ]
        }
    ]
}
```
+  For API details, see [GetCorsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html) in *AWS CLI Command Reference*.

### `get-lifecycle-policy`
<a name="mediastore_GetLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `get-lifecycle-policy`.

**AWS CLI**
**To view an object lifecycle policy**
The following `get-lifecycle-policy` example displays the object lifecycle policy attached to the specified container.

```
aws mediastore get-lifecycle-policy \
    --container-name {{LiveEvents}}
```
Output:

```
{
    "LifecyclePolicy": "{\"rules\":[{\"definition\":{\"path\":[{\"prefix\":\"Football/\"},{\"prefix\":\"Baseball/\"}],\"days_since_create\":[{\"numeric\":[\">\",28]}]},\"action\":\"EXPIRE\"}]}"
}
```
+  For API details, see [GetLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-lifecycle-policy.html) in *AWS CLI Command Reference*.

### `list-containers`
<a name="mediastore_ListContainers_cli_2_topic"></a>

The following code example shows how to use `list-containers`.

**AWS CLI**
**To view a list of containers**
The following `list-containers` example displays a list of all containers that are associated with your account.

```
aws mediastore list-containers
```
Output:

```
{
    "Containers": [
        {
            "CreationTime": 1505317931,
            "Endpoint": "https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com",
            "Status": "ACTIVE",
            "ARN": "arn:aws:mediastore:us-west-2:123456789012:container/ExampleLiveDemo",
            "AccessLoggingEnabled": false,
            "Name": "ExampleLiveDemo"
        },
        {
            "CreationTime": 1506528818,
            "Endpoint": "https://fffggghhhiiijj.data.mediastore.us-west-2.amazonaws.com",
            "Status": "ACTIVE",
            "ARN": "arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer",
            "AccessLoggingEnabled": false,
            "Name": "ExampleContainer"
        }
    ]
}
```
+  For API details, see [ListContainers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-containers.html) in *AWS CLI Command Reference*.

### `list-tags-for-resource`
<a name="mediastore_ListTagsForResource_cli_2_topic"></a>

The following code example shows how to use `list-tags-for-resource`.

**AWS CLI**
**To list tags for a container**
The following `list-tags-for-resource` example displays the tag keys and values assigned to the specified container.

```
aws mediastore list-tags-for-resource \
    --resource {{arn:aws:mediastore:us-west-2:1213456789012:container/ExampleContainer}}
```
Output:

```
{
    "Tags": [
        {
            "Value": "Test",
            "Key": "Environment"
        },
        {
            "Value": "West",
            "Key": "Region"
        }
    ]
}
```
For more information, see [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in the *Tagging AWS Resources and Tag Editor User Guide*.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-tags-for-resource.html) in *AWS CLI Command Reference*.

### `put-container-policy`
<a name="mediastore_PutContainerPolicy_cli_2_topic"></a>

The following code example shows how to use `put-container-policy`.

**AWS CLI**
**To edit a container policy**
The following `put-container-policy` example assigns a different policy to the specified container. In this example, the updated policy is defined in a file named `LiveEventsContainerPolicy.json`.

```
aws mediastore put-container-policy \
    --container-name {{LiveEvents}} \
    --policy {{file://LiveEventsContainerPolicy.json}}
```
Contents of `LiveEventsContainerPolicy.json`:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "MediaStoreFullAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:root"
            },
            "Action": "mediastore:*",
            "Resource": "arn:aws:mediastore:us-west-2:123456789012:container/LiveEvents/*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                }
            }
        }
    ]
}
```
This command produces no output.
+  For API details, see [PutContainerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-container-policy.html) in *AWS CLI Command Reference*.

### `put-cors-policy`
<a name="mediastore_PutCorsPolicy_cli_2_topic"></a>

The following code example shows how to use `put-cors-policy`.

**AWS CLI**
**Example 1: To add a CORS policy**
The following `put-cors-policy` example adds a cross-origin resource sharing (CORS) policy to the specified container. The contents of the CORS policy are in the file named `corsPolicy.json`.

```
aws mediastore put-cors-policy \
    --container-name {{ExampleContainer}} \
    --cors-policy {{file://corsPolicy.json}}
```
Contents of `corsPolicy.json`:

```
[
    {
        "AllowedOrigins": [
            "https://www.example.com"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD"
        ],
        "AllowedHeaders": [
            "*"
        ],
        "MaxAgeSeconds": 3000
    }
]
```
This command produces no output.
**Example 2: To edit a CORS policy**
The following `put-cors-policy` example updates the cross-origin resource sharing (CORS) policy that is assigned to the specified container. The contents of the updated CORS policy are in the file named `corsPolicy2.json`.
+  For API details, see [PutCorsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html) in *AWS CLI Command Reference*.

### `put-lifecycle-policy`
<a name="mediastore_PutLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `put-lifecycle-policy`.

**AWS CLI**
**To create an object lifecycle policy**
The following `put-lifecycle-policy` example attaches an object lifecycle policy to the specified container. This enables you to specify how long the service should store objects in your container. MediaStore deletes objects in the container once they reach their expiration date, as indicated in the policy, which is in the file named `ExampleLifecyclePolicy.json`.

```
aws mediastore put-lifecycle-policy \
    --container-name {{ExampleContainer}} \
    --lifecycle-policy {{file://ExampleLifecyclePolicy.json}}
```
Contents of `ExampleLifecyclePolicy.json`:

```
{
    "rules": [
        {
            "definition": {
                "path": [
                    {"prefix": "Football/"},
                    {"prefix": "Baseball/"}
                ],
                "days_since_create": [
                    {"numeric": [">", 28]}
                ]
            },
            "action": "EXPIRE"
        }
    ]
}
```
This command produces no output.
+  For API details, see [PutLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-lifecycle-policy.html) in *AWS CLI Command Reference*.

### `start-access-logging`
<a name="mediastore_StartAccessLogging_cli_2_topic"></a>

The following code example shows how to use `start-access-logging`.

**AWS CLI**
**To enable access logging on a container**
The following `start-access-logging` example enable access logging on the specified container.

```
aws mediastore start-access-logging \
    --container-name {{LiveEvents}}
```
This command produces no output.
+  For API details, see [StartAccessLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/start-access-logging.html) in *AWS CLI Command Reference*.

### `stop-access-logging`
<a name="mediastore_StopAccessLogging_cli_2_topic"></a>

The following code example shows how to use `stop-access-logging`.

**AWS CLI**
**To disable access logging on a container**
The following `stop-access-logging` example disables access logging on the specified container.

```
aws mediastore stop-access-logging \
    --container-name {{LiveEvents}}
```
This command produces no output.
+  For API details, see [StopAccessLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/stop-access-logging.html) in *AWS CLI Command Reference*.

### `tag-resource`
<a name="mediastore_TagResource_cli_2_topic"></a>

The following code example shows how to use `tag-resource`.

**AWS CLI**
**To add tags to a container**
The following `tag-resource` example adds tag keys and values to the specified container.

```
aws mediastore tag-resource \
    --resource {{arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer}} \
    --tags '{{[{"Key": "Region", "Value": "West"}, {"Key": "Environment", "Value": "Test"}]}}'
```
This command produces no output.
For more information, see [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in the *Tagging AWS Resources and Tag Editor User Guide*.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/tag-resource.html) in *AWS CLI Command Reference*.

### `untag-resource`
<a name="mediastore_UntagResource_cli_2_topic"></a>

The following code example shows how to use `untag-resource`.

**AWS CLI**
**To remove tags from a container**
The following `untag-resource` example removes the specified tag key and its associated value from a container.

```
aws mediastore untag-resource \
    --resource {{arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer}} \
    --tag-keys {{Region}}
```
This command produces no output.
For more information, see [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in the *Tagging AWS Resources and Tag Editor User Guide*.
+  For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/untag-resource.html) in *AWS CLI Command Reference*.
