---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-map-role.html
---

# Step 4: Map the migration role on the target domain
<a name="pb-es68-map-role"></a>

If your Amazon OpenSearch Service domain has fine-grained access control enabled, the migration IAM role must be allowed to write metadata and documents. Map it as the domain’s master user (the Amazon OpenSearch Service fine-grained access control administrative user) by updating the domain’s advanced security options. Replace `<DOMAIN_NAME>` and the role ARN with your values:

```
aws opensearch update-domain-config \
  --domain-name <DOMAIN_NAME> \
  --advanced-security-options '{
    "MasterUserOptions": {
      "MasterUserARN": "arn:aws:iam::<ACCOUNT_ID>:role/<eks-cluster-name>-migrations-role"
    }
  }' \
  --region <REGION>
```

**Note**
Granting the migration role broad access (for example, an `all_access`-equivalent role) is convenient during migration. Scope the permissions down or remove the mapping after cutover so the migration role no longer has standing write access to the domain. See [Security](security-1.md).
