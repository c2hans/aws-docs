---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_05_multi-user-ad-step4.html
---

# Connect to the cluster as a user
<a name="tutorials_05_multi-user-ad-step4"></a>

You can determine the status of the cluster with the following commands.

```
$ pcluster describe-cluster -n {{ad-cluster}} --region {{"region-id"}} --query "clusterStatus"
```

The output is as follows.

```
"CREATE_IN_PROGRESS" / "CREATE_COMPLETE"
```

When the status reaches `"CREATE_COMPLETE"`, log in with the created user name and password.

```
$ HEAD_NODE_IP=$(pcluster describe-cluster -n {{"ad-cluster"}} --region {{"region-id"}} --query headNode.publicIpAddress | xargs echo)
```

```
$ ssh {{user000}}@$HEAD_NODE_IP
```

You can log in without the password by providing the SSH key that was created for the new user at `/home/user000@HEAD_NODE_IP/.ssh/id_rsa`.

If the `ssh` command succeeded, you have successfully connected to the cluster as a user that's authenticated to use the Active Directory (AD).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
