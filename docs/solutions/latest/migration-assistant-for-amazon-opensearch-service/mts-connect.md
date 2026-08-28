---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/mts-connect.html
---

# Connect your collection to Migration Assistant
<a name="mts-connect"></a>

Migration Assistant authenticates to an Amazon OpenSearch Serverless NextGen collection with [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) (SigV4) using the credentials of the migration IAM role created during deployment. Before the workflow can write to your collection, you grant that role access through the collection’s data access policy and point the target configuration at the collection endpoint.

## Step 1: Find the migration IAM role
<a name="mts-step1-find-role"></a>

The Amazon EKS deployment creates an IAM role named `<eks-cluster-name>-migrations-role`. Both the Migration Console pod and the Argo workflow executor pods receive this role’s credentials automatically through Amazon EKS Pod Identity. Locate the role and its Amazon Resource Name (ARN) so you can add it to the collection data access policy:

```
aws iam list-roles \
  --query "Roles[?contains(RoleName,'migrations-role')].{Name:RoleName,Arn:Arn}" \
  --output table
```

Record the ARN of the role that matches your Amazon EKS cluster name.

## Step 2: Update the collection data access policy
<a name="mts-step2-access-policy"></a>

Grant the migration IAM role access to the collection and its indexes with an [Amazon OpenSearch Serverless NextGen data access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html). Create a JSON policy document that grants collection-level and index-level permissions to the role ARN from Step 1, then create the policy:

```
[
  {
    "Rules": [
      {
        "ResourceType": "collection",
        "Resource": ["collection/<collection-name>"],
        "Permission": [
          "aoss:CreateCollectionItems",
          "aoss:DeleteCollectionItems",
          "aoss:UpdateCollectionItems",
          "aoss:DescribeCollectionItems"
        ]
      },
      {
        "ResourceType": "index",
        "Resource": ["index/<collection-name>/*"],
        "Permission": [
          "aoss:CreateIndex",
          "aoss:DeleteIndex",
          "aoss:UpdateIndex",
          "aoss:DescribeIndex",
          "aoss:ReadDocument",
          "aoss:WriteDocument"
        ]
      }
    ],
    "Principal": ["arn:aws:iam::<account-id>:role/<eks-cluster-name>-migrations-role"]
  }
]
```

```
aws opensearchserverless create-access-policy \
  --name migration-assistant-access \
  --type data \
  --policy file://data-access-policy.json
```

In addition to the data access policy, the migration IAM role’s IAM permissions policy must allow `aoss:APIAccessAll` on the collection so that it can call the collection’s data plane API. If the workflow later fails with HTTP 403 against the collection, confirm both the data access policy principal and the `aoss:APIAccessAll` IAM permission. See [Troubleshooting](troubleshooting.md).

## Step 3: Configure the workflow target
<a name="mts-step3-target-config"></a>

Edit the workflow configuration with `workflow configure edit` and set the target cluster to your collection endpoint. For an Amazon OpenSearch Serverless NextGen collection, set the SigV4 `service` to `aoss` (for an Amazon OpenSearch Service domain it is `es`), and use the collection endpoint in the form `https://<collection-id>.<region>.aoss.amazonaws.com`:

```
{
  "targetClusters": {
    "target": {
      "endpoint": "https://<collection-id>.<region>.aoss.amazonaws.com",
      "authConfig": {
        "sigv4": {
          "region": "<region>",
          "service": "aoss"
        }
      }
    }
  }
}
```

Before you submit the workflow, verify that the Migration Console can reach and authenticate to the collection:

```
console clusters connection-check --cluster target
aws sts get-caller-identity
```

If the connection check fails, stop and resolve the data access policy or `aoss:APIAccessAll` permission before continuing. Do not start a workflow until the target check passes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
