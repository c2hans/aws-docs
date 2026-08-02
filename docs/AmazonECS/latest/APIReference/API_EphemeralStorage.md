---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_EphemeralStorage.html
---

# EphemeralStorage
<a name="API_EphemeralStorage"></a>

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate. For more information, see [Using data volumes in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) in the *Amazon ECS Developer Guide;*.

**Note**
For tasks using the Fargate launch type, the task requires the following platforms:
Linux platform version `1.4.0` or later.
Windows platform version `1.0.0` or later.

## Contents
<a name="API_EphemeralStorage_Contents"></a>

 ** sizeInGiB **   <a name="ECS-Type-EphemeralStorage-sizeInGiB"></a>
The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.
Type: Integer
Required: Yes

## See Also
<a name="API_EphemeralStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/EphemeralStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/EphemeralStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/EphemeralStorage)
