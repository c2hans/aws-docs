---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-create-security-policies.html
---

# Step 1: Create the Serverless security policies
<a name="pb-aoss-create-security-policies"></a>

Create the collection’s security policies **before** you create the collection. A collection that comes up without a matching encryption policy fails, and without network and data access policies the migration cannot write to it. Create them in this order: encryption, network, then the data access policy.

## Create the encryption policy
<a name="pb-aoss-encryption-policy"></a>

The encryption policy selects the [AWS Key Management Service](https://aws.amazon.com/kms) (AWS KMS) key that protects the collection’s data at rest. The following example uses an AWS owned key (`AWSOwnedKey: true`) and matches a single collection named `vector-search`:

```
aws opensearchserverless create-security-policy \
  --name vector-search-encryption \
  --type encryption \
  --policy '{
    "Rules": [
      { "ResourceType": "collection", "Resource": ["collection/vector-search"] }
    ],
    "AWSOwnedKey": true
  }'
```

## Create the network policy
<a name="pb-aoss-network-policy"></a>

The network policy controls whether the collection endpoint (and its OpenSearch Dashboards endpoint) is reachable from public networks or only from OpenSearch Serverless-managed VPC endpoints. Choose the access pattern that matches how the Amazon EKS cluster reaches the collection.

For a collection reachable over public networks:

```
aws opensearchserverless create-security-policy \
  --name vector-search-network \
  --type network \
  --policy '[
    {
      "Description": "Public access for vector-search collection",
      "Rules": [
        { "ResourceType": "collection", "Resource": ["collection/vector-search"] },
        { "ResourceType": "dashboard",  "Resource": ["collection/vector-search"] }
      ],
      "AllowFromPublic": true
    }
  ]'
```

For private (VPC-only) access, set `"AllowFromPublic": false` and list your OpenSearch Serverless-managed VPC endpoints in a `SourceVPCEs` array. The Amazon EKS cluster must be able to reach one of those endpoints.

**Note**
Even with public network access, the data access policy still controls which IAM principals can read or write data. Network access only determines which networks can reach the endpoint.

## Create the data access policy
<a name="pb-aoss-data-access-policy"></a>

The data access policy grants the migration IAM role the collection- and index-level permissions it needs to create indexes and bulk-index documents. The principal is the migration role created by the Amazon EKS deployment, named `<eks-cluster-name>-migrations-role`.

```
aws opensearchserverless create-access-policy \
  --name vector-search-data \
  --type data \
  --policy '[
    {
      "Description": "Migration write access for vector-search",
      "Rules": [
        {
          "ResourceType": "collection",
          "Resource": ["collection/vector-search"],
          "Permission": ["aoss:CreateCollectionItems", "aoss:DescribeCollectionItems"]
        },
        {
          "ResourceType": "index",
          "Resource": ["index/vector-search/*"],
          "Permission": ["aoss:CreateIndex", "aoss:UpdateIndex", "aoss:DescribeIndex", "aoss:WriteDocument", "aoss:ReadDocument"]
        }
      ],
      "Principal": ["arn:aws:iam::<ACCOUNT_ID>:role/<eks-cluster-name>-migrations-role"]
    }
  ]'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
