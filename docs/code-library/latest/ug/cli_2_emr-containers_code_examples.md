---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_emr-containers_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon EMR on EKS examples using AWS CLI
<a name="cli_2_emr-containers_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EMR on EKS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-role-associations`
<a name="emr-containers_CreateRoleAssociations_cli_2_topic"></a>

The following code example shows how to use `create-role-associations`.

**AWS CLI**
**To create role associations of an IAM Role with EMR service accounts to be used with Amazon EMR on EKS**
The following `create-role-associations` example command creates EKS pod identity associations of a role named **example\_iam\_role** with EMR service accounts such that it can be used with Amazon EMR on EKS with **example\_namespace** namespace from an EKS cluster named **example\_cluster**.:

```
aws emr-containers create-role-associations \
    --cluster-name {{example_cluster}} \
    --namespace {{example_namespace}} \
    --role-name {{example_iam_role}}
```
Output:

```
[
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-client-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/a-bgyr1umgdmrk1kdtq",
        "associationId": "a-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    },
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-driver-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/b-bgyr1umgdmrk1kdtq",
        "associationId": "b-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    },
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-executor-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/c-bgyr1umgdmrk1kdtq",
        "associationId": "c-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    }
]
```
+  For API details, see [CreateRoleAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-role-associations.html) in *AWS CLI Command Reference*.

### `delete-role-associations`
<a name="emr-containers_DeleteRoleAssociations_cli_2_topic"></a>

The following code example shows how to use `delete-role-associations`.

**AWS CLI**
**To delete role associations of an IAM Role with EMR service accounts**
EKS allows associations with non existing resources (namespace, service account), so EMR on EKS suggest to delete the associations if the namespace is deleted or the role is not in use to release the space for other associations.
The following `delete-role-associations` example command deletes EKS pod identity associations of a role named **example\_iam\_role** with EMR service accounts such that it can be removed from Amazon EMR on EKS with **example\_namespace** namespace from an EKS cluster named **example\_cluster**.:

```
aws emr-containers delete-role-associations \
    --cluster-name {{example_cluster}} \
    --namespace {{example_namespace}} \
    --role-name {{example_iam_role}}
```
Output:

```
[
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-client-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/a-bgyr1umgdmrk1kdtq",
        "associationId": "a-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    },
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-driver-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/b-bgyr1umgdmrk1kdtq",
        "associationId": "b-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    },
    {
        "clusterName": "example_cluster",
        "namespace": "example_namespace",
        "serviceAccount": "emr-spark-executor-service-account-example",
        "roleArn": "arn:aws:iam::111111111111:role/example_iam_role",
        "associationArn": "arn:aws:eks:us-east-1:111111111111:podidentityassociation/example_cluster/c-bgyr1umgdmrk1kdtq",
        "associationId": "c-bgyr1umgdmrk1kdtq",
        "tags": {},
        "createdAt": "2022-11-15T10:49:00+00:00",
        "modifiedAt": "2022-11-15T10:49:00+00:00"
    }
]
```
+  For API details, see [DeleteRoleAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/delete-role-associations.html) in *AWS CLI Command Reference*.

### `update-role-trust-policy`
<a name="emr-containers_UpdateRoleTrustPolicy_cli_2_topic"></a>

The following code example shows how to use `update-role-trust-policy`.

**AWS CLI**
**To update the trust policy of an IAM Role to be used with Amazon EMR on EKS**
This example command updates the trust policy of a role named **example\_iam\_role** such that it can be used with Amazon EMR on EKS with **example\_namespace** namespace from an EKS cluster named **example\_cluster**.
Command:

```
aws emr-containers update-role-trust-policy \
    --cluster example_cluster \
    --namespace example_namespace \
    --role-name example_iam_role
```
Output:

```
If the trust policy has already been updated, then the output will be:
Trust policy statement already exists for role example_iam_role. No
changes were made!

If the trust policy has not been updated yet, then the output will be:
Successfully updated trust policy of role example_iam_role.
```
+  For API details, see [UpdateRoleTrustPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/update-role-trust-policy.html) in *AWS CLI Command Reference*.
