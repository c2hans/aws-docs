---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-console.html
---

# Step 5: Access the Migration Console and create secrets
<a name="pb-es68-console"></a>

The day-to-day operator interface is the Workflow CLI, which runs in the Migration Console pod (`migration-console-0`) in the `ma` namespace on Amazon EKS.

1. Refresh your kubeconfig if you are in a new shell:

   ```
   aws eks update-kubeconfig --region <REGION> --name migration-eks-cluster-<STAGE>-<REGION>
   ```

1. Open a shell in the Migration Console pod:

   ```
   kubectl exec -it migration-console-0 -n ma -- /bin/bash
   ```

1. Confirm the installed version so you load a matching workflow schema:

   ```
   console --version
   ```

1. If the source cluster uses basic authentication, create managed HTTP Basic credentials in the `ma` namespace. The target uses SigV4 in this playbook, so it does not need a basic-auth secret:

   ```
   workflow configure credentials create source-credentials
   ```

   You reference this credential by name in `authConfig.basic.secretName` in the workflow configuration. For non-interactive setup, use `workflow configure credentials create source-credentials --stdin` and pass one `USERNAME:PASSWORD` line on stdin.
