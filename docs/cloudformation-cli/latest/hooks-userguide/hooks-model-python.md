---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model-python.html
---

# Modeling custom CloudFormation Hooks using Python
<a name="hooks-model-python"></a>

Modeling custom CloudFormation Hooks involves creating a schema that defines the Hook, its properties, and their attributes. This tutorial walks you through modeling custom Hooks using Python.

## Step 1: Generate the Hook project package
<a name="model-hook-project-package-python"></a>

Generate your Hook project package. The CloudFormation CLI creates empty handler functions that correspond to specific Hook actions in the target lifecycle as defined in the Hook specification.

```
cfn generate
```

The command returns the following output.

```
Generated files for MyCompany::Testing::MyTestHook
```

**Note**
Make sure your Lambda runtimes are up-to-date to avoid using a deprecated version. For more information, see [Updating Lambda runtimes for resource types and Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/runtime-update.html).

## Step 2: Add Hook handlers
<a name="model-hook-project-add-handler"></a>

Add your own Hook handler runtime code to the handlers that you choose to implement. For example, you can add the following code for logging.

```
LOG.setLevel(logging.INFO)
LOG.info("Internal testing Hook triggered for target: " + request.hookContext.targetName);
```

The CloudFormation CLI generates the `src/models.py` file from the [Hook configuration schema syntax reference](hook-configuration-schema.md).

**Example models.py**

```
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseHookHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")

def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None

@dataclass
class HookHandlerRequest(BaseHookHandlerRequest):
    pass

@dataclass
class TypeConfigurationModel(BaseModel):
    limitSize: Optional[str]
    cidr: Optional[str]
    encryptionAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls(
            limitSize=json_data.get("limitSize"),
            cidr=json_data.get("cidr"),
            encryptionAlgorithm=json_data.get("encryptionAlgorithm"),
        )

_TypeConfigurationModel = TypeConfigurationModel
```

## Step 3: Implement Hook handlers
<a name="model-hook-project-code-handler-python"></a>

With the Python data classes generated, you can write the handlers that actually implement the Hook’s functionality. In this example, you’ll implement the `preCreate`, `preUpdate`, and `preDelete` invocation points for the handlers.

**Topics**
+ [Implement the preCreate handler](#model-hook-project-code-handler-python-precreate)
+ [Implement the preUpdate handler](#model-hook-project-code-handler-python-preupdate)
+ [Implement the preDelete handler](#model-hook-project-code-handler-python-predelete)
+ [Implement a Hook handler](#model-hook-project-code-handler-python-hook-handler)

### Implement the preCreate handler
<a name="model-hook-project-code-handler-python-precreate"></a>

The `preCreate` handler verifies the server-side encryption settings for either an `AWS::S3::Bucket ` or `AWS::SQS::Queue` resource.
+ For an `AWS::S3::Bucket` resource, the Hook will only pass if the following is true.
  + The Amazon S3 bucket encryption is set.
  + The Amazon S3 bucket key is enabled for the bucket.
  + The encryption algorithm set for the Amazon S3 bucket is the correct algorithm required.
  + The AWS Key Management Service key ID is set.
+ For an `AWS::SQS::Queue` resource, the Hook will only pass if the following is true.
  + The AWS Key Management Service key ID is set.

### Implement the preUpdate handler
<a name="model-hook-project-code-handler-python-preupdate"></a>

Implement a `preUpdate` handler, which initiates before the update operations for all specified targets in the handler. The `preUpdate` handler accomplishes the following:
+ For an `AWS::S3::Bucket` resource, the Hook will only pass if the following is true:
  + The bucket encryption algorithm for an Amazon S3 bucket hasn't been modified.

### Implement the preDelete handler
<a name="model-hook-project-code-handler-python-predelete"></a>

Implement a `preDelete` handler, which initiates before the delete operations for all specified targets in the handler. The `preDelete` handler accomplishes the following:
+ For an `AWS::S3::Bucket` resource, the Hook will only pass if the following is true:
  + Verifies that the minimum required compliant resources will exist in the account after delete the resource.
  + The minimum required compliant resources amount is set in the Hook’s configuration.

### Implement a Hook handler
<a name="model-hook-project-code-handler-python-hook-handler"></a>

1. In your IDE, open the `handlers.py` file, located in the `src` folder.

1. Replace the entire contents of the `handlers.py` file with the following code.
**Example handlers.py**

   ```
   import logging
   from typing import Any, MutableMapping, Optional
   import botocore

   from cloudformation_cli_python_lib import (
       BaseHookHandlerRequest,
       HandlerErrorCode,
       Hook,
       HookInvocationPoint,
       OperationStatus,
       ProgressEvent,
       SessionProxy,
       exceptions,
   )

   from .models import HookHandlerRequest, TypeConfigurationModel

   # Use this logger to forward log messages to CloudWatch Logs.
   LOG = logging.getLogger(__name__)
   TYPE_NAME = "MyCompany::Testing::MyTestHook"

   LOG.setLevel(logging.INFO)

   hook = Hook(TYPE_NAME, TypeConfigurationModel)
   test_entrypoint = hook.test_entrypoint

   def _validate_s3_bucket_encryption(
       bucket: MutableMapping[str, Any], required_encryption_algorithm: str
   ) -> ProgressEvent:
       status = None
       message = ""
       error_code = None

       if bucket:
           bucket_name = bucket.get("BucketName")

           bucket_encryption = bucket.get("BucketEncryption")
           if bucket_encryption:
               server_side_encryption_rules = bucket_encryption.get(
                   "ServerSideEncryptionConfiguration"
               )
               if server_side_encryption_rules:
                   for rule in server_side_encryption_rules:
                       bucket_key_enabled = rule.get("BucketKeyEnabled")
                       if bucket_key_enabled:
                           server_side_encryption_by_default = rule.get(
                               "ServerSideEncryptionByDefault"
                           )

                           encryption_algorithm = server_side_encryption_by_default.get(
                               "SSEAlgorithm"
                           )
                           kms_key_id = server_side_encryption_by_default.get(
                               "KMSMasterKeyID"
                           )  # "KMSMasterKeyID" is name of the property for an AWS::S3::Bucket

                           if encryption_algorithm == required_encryption_algorithm:
                               if encryption_algorithm == "aws:kms" and not kms_key_id:
                                   status = OperationStatus.FAILED
                                   message = f"KMS Key ID not set for bucket with name: f{bucket_name}"
                               else:
                                   status = OperationStatus.SUCCESS
                                   message = f"Successfully invoked PreCreateHookHandler for AWS::S3::Bucket with name: {bucket_name}"
                           else:
                               status = OperationStatus.FAILED
                               message = f"SSE Encryption Algorithm is incorrect for bucket with name: {bucket_name}"
                       else:
                           status = OperationStatus.FAILED
                           message = f"Bucket key not enabled for bucket with name: {bucket_name}"

                       if status == OperationStatus.FAILED:
                           break
               else:
                   status = OperationStatus.FAILED
                   message = f"No SSE Encryption configurations for bucket with name: {bucket_name}"
           else:
               status = OperationStatus.FAILED
               message = (
                   f"Bucket Encryption not enabled for bucket with name: {bucket_name}"
               )
       else:
           status = OperationStatus.FAILED
           message = "Resource properties for S3 Bucket target model are empty"

       if status == OperationStatus.FAILED:
           error_code = HandlerErrorCode.NonCompliant

       return ProgressEvent(status=status, message=message, errorCode=error_code)

   def _validate_sqs_queue_encryption(queue: MutableMapping[str, Any]) -> ProgressEvent:
       if not queue:
           return ProgressEvent(
               status=OperationStatus.FAILED,
               message="Resource properties for SQS Queue target model are empty",
               errorCode=HandlerErrorCode.NonCompliant,
           )
       queue_name = queue.get("QueueName")

       kms_key_id = queue.get(
           "KmsMasterKeyId"
       )  # "KmsMasterKeyId" is name of the property for an AWS::SQS::Queue
       if not kms_key_id:
           return ProgressEvent(
               status=OperationStatus.FAILED,
               message=f"Server side encryption turned off for queue with name: {queue_name}",
               errorCode=HandlerErrorCode.NonCompliant,
           )

       return ProgressEvent(
           status=OperationStatus.SUCCESS,
           message=f"Successfully invoked PreCreateHookHandler for targetAWS::SQS::Queue with name: {queue_name}",
       )

   @hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
   def pre_create_handler(
       session: Optional[SessionProxy],
       request: HookHandlerRequest,
       callback_context: MutableMapping[str, Any],
       type_configuration: TypeConfigurationModel,
   ) -> ProgressEvent:
       target_name = request.hookContext.targetName
       if "AWS::S3::Bucket" == target_name:
           return _validate_s3_bucket_encryption(
               request.hookContext.targetModel.get("resourceProperties"),
               type_configuration.encryptionAlgorithm,
           )
       elif "AWS::SQS::Queue" == target_name:
           return _validate_sqs_queue_encryption(
               request.hookContext.targetModel.get("resourceProperties")
           )
       else:
           raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

   def _validate_bucket_encryption_rules_not_updated(
       resource_properties, previous_resource_properties
   ) -> ProgressEvent:
       bucket_encryption_configs = resource_properties.get("BucketEncryption", {}).get(
           "ServerSideEncryptionConfiguration", []
       )
       previous_bucket_encryption_configs = previous_resource_properties.get(
           "BucketEncryption", {}
       ).get("ServerSideEncryptionConfiguration", [])

       if len(bucket_encryption_configs) != len(previous_bucket_encryption_configs):
           return ProgressEvent(
               status=OperationStatus.FAILED,
               message=f"Current number of bucket encryption configs does not match previous. Current has {str(len(bucket_encryption_configs))} configs while previously there were {str(len(previous_bucket_encryption_configs))} configs",
               errorCode=HandlerErrorCode.NonCompliant,
           )

       for i in range(len(bucket_encryption_configs)):
           current_encryption_algorithm = (
               bucket_encryption_configs[i]
               .get("ServerSideEncryptionByDefault", {})
               .get("SSEAlgorithm")
           )
           previous_encryption_algorithm = (
               previous_bucket_encryption_configs[i]
               .get("ServerSideEncryptionByDefault", {})
               .get("SSEAlgorithm")
           )

           if current_encryption_algorithm != previous_encryption_algorithm:
               return ProgressEvent(
                   status=OperationStatus.FAILED,
                   message=f"Bucket Encryption algorithm can not be changed once set. The encryption algorithm was changed to {current_encryption_algorithm} from {previous_encryption_algorithm}.",
                   errorCode=HandlerErrorCode.NonCompliant,
               )

       return ProgressEvent(
           status=OperationStatus.SUCCESS,
           message="Successfully invoked PreUpdateHookHandler for target: AWS::SQS::Queue",
       )

   def _validate_queue_encryption_not_disabled(
       resource_properties, previous_resource_properties
   ) -> ProgressEvent:
       if previous_resource_properties.get(
           "KmsMasterKeyId"
       ) and not resource_properties.get("KmsMasterKeyId"):
           return ProgressEvent(
               status=OperationStatus.FAILED,
               errorCode=HandlerErrorCode.NonCompliant,
               message="Queue encryption can not be disable",
           )
       else:
           return ProgressEvent(status=OperationStatus.SUCCESS)

   @hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
   def pre_update_handler(
       session: Optional[SessionProxy],
       request: BaseHookHandlerRequest,
       callback_context: MutableMapping[str, Any],
       type_configuration: MutableMapping[str, Any],
   ) -> ProgressEvent:
       target_name = request.hookContext.targetName
       if "AWS::S3::Bucket" == target_name:
           resource_properties = request.hookContext.targetModel.get("resourceProperties")
           previous_resource_properties = request.hookContext.targetModel.get(
               "previousResourceProperties"
           )

           return _validate_bucket_encryption_rules_not_updated(
               resource_properties, previous_resource_properties
           )
       elif "AWS::SQS::Queue" == target_name:
           resource_properties = request.hookContext.targetModel.get("resourceProperties")
           previous_resource_properties = request.hookContext.targetModel.get(
               "previousResourceProperties"
           )

           return _validate_queue_encryption_not_disabled(
               resource_properties, previous_resource_properties
           )
       else:
           raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")
   ```

Continue to the next topic [Registering a custom Hook with CloudFormation](registering-hooks.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
