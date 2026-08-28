---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_update_troubleshooting.html
---

# Troubleshooting AWS PCS cluster updates
<a name="working-with_clusters_update_troubleshooting"></a>

This topic helps you identify and resolve common problems that can occur when updating cluster configurations.

## Update fails with accounting configuration error
<a name="update-fails-accounting-error"></a>

### Common cause
<a name="accounting-error-cause"></a>

The cluster enters `UPDATE_FAILED` state and the error message indicates an accounting configuration issue. This typically occurs when the accounting configuration is incompatible with the current Slurm version or contains invalid settings.

### Resolution
<a name="accounting-error-resolution"></a>

Review your accounting settings for compatibility with your cluster's Slurm version and submit a corrected update request with valid configuration parameters.

## Update fails with custom settings error
<a name="update-fails-custom-settings-error"></a>

### Common cause
<a name="custom-settings-error-cause"></a>

The cluster enters `UPDATE_FAILED` state and the error message indicates a Slurm custom settings issue. This occurs when you provide invalid Slurm parameter values or unsupported parameter combinations.

### Resolution
<a name="custom-settings-error-resolution"></a>

Validate your Slurm custom settings against the supported parameters and submit a corrected update request with valid parameter values and combinations.

## Cannot submit update request
<a name="cannot-submit-update-request"></a>

### Common cause
<a name="submit-error-cause"></a>

The update button is disabled in the console or the API returns a 400-level error. This occurs when the cluster is not in an appropriate state, associated resources are not active, or there are validation failures in your configuration.

### Resolution
<a name="submit-error-resolution"></a>

Wait for the cluster and all associated resources to reach `ACTIVE` state, then review your configuration for validation errors before resubmitting the update request.

## Validation errors
<a name="validation-errors"></a>

### Common cause
<a name="validation-cause"></a>

The command returns immediately with a 400-level HTTP error and descriptive message. This occurs due to invalid cluster state, resource state, or configuration parameters.

### Resolution
<a name="validation-resolution"></a>

Address the specific validation error mentioned in the response and retry the update operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
