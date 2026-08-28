---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsDetails"></a>

A container definition that describes a container in the task.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsDetails_Contents"></a>

 ** Command **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Command"></a>
The command that is passed to the container.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Cpu **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Cpu"></a>
The number of CPU units reserved for the container.
Type: Integer
Required: No

 ** DependsOn **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-DependsOn"></a>
The dependencies that are defined for container startup and shutdown.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails](API_AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails.md) objects
Required: No

 ** DisableNetworking **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-DisableNetworking"></a>
Whether to disable networking within the container.
Type: Boolean
Required: No

 ** DnsSearchDomains **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-DnsSearchDomains"></a>
A list of DNS search domains that are presented to the container.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** DnsServers **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-DnsServers"></a>
A list of DNS servers that are presented to the container.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** DockerLabels **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-DockerLabels"></a>
A key-value map of labels to add to the container.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** DockerSecurityOptions **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-DockerSecurityOptions"></a>
A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** EntryPoint **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-EntryPoint"></a>
The entry point that is passed to the container.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Environment **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Environment"></a>
The environment variables to pass to a container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails](API_AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails.md) objects
Required: No

 ** EnvironmentFiles **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-EnvironmentFiles"></a>
A list of files containing the environment variables to pass to a container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails](API_AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails.md) objects
Required: No

 ** Essential **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Essential"></a>
Whether the container is essential. All tasks must have at least one essential container.
Type: Boolean
Required: No

 ** ExtraHosts **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-ExtraHosts"></a>
A list of hostnames and IP address mappings to append to the **/etc/hosts** file on the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails.md) objects
Required: No

 ** FirelensConfiguration **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-FirelensConfiguration"></a>
The FireLens configuration for the container. Specifies and configures a log router for container logs.
Type: [AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails](API_AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails.md) object
Required: No

 ** HealthCheck **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-HealthCheck"></a>
The container health check command and associated configuration parameters for the container.
Type: [AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails](API_AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails.md) object
Required: No

 ** Hostname **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Hostname"></a>
The hostname to use for the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Image **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Image"></a>
The image used to start the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Interactive **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Interactive"></a>
If set to true, then containerized applications can be deployed that require `stdin` or a `tty` to be allocated.
Type: Boolean
Required: No

 ** Links **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Links"></a>
A list of links for the container in the form ` container_name:alias `. Allows containers to communicate with each other without the need for port mappings.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** LinuxParameters **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-LinuxParameters"></a>
Linux-specific modifications that are applied to the container, such as Linux kernel capabilities.
Type: [AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails](API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails.md) object
Required: No

 ** LogConfiguration **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-LogConfiguration"></a>
The log configuration specification for the container.
Type: [AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails](API_AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails.md) object
Required: No

 ** Memory **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Memory"></a>
The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is shut down. The total amount of memory reserved for all containers within a task must be lower than the task memory value, if one is specified.
Type: Integer
Required: No

 ** MemoryReservation **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-MemoryReservation"></a>
The soft limit (in MiB) of memory to reserve for the container.
Type: Integer
Required: No

 ** MountPoints **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-MountPoints"></a>
The mount points for the data volumes in the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails.md) objects
Required: No

 ** Name **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Name"></a>
The name of the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PortMappings **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-PortMappings"></a>
The list of port mappings for the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails.md) objects
Required: No

 ** Privileged **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Privileged"></a>
Whether the container is given elevated privileges on the host container instance. The elevated privileges are similar to the root user.
Type: Boolean
Required: No

 ** PseudoTerminal **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-PseudoTerminal"></a>
Whether to allocate a TTY to the container.
Type: Boolean
Required: No

 ** ReadonlyRootFilesystem **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-ReadonlyRootFilesystem"></a>
Whether the container is given read-only access to its root file system.
Type: Boolean
Required: No

 ** RepositoryCredentials **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-RepositoryCredentials"></a>
The private repository authentication credentials to use.
Type: [AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails.md) object
Required: No

 ** ResourceRequirements **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-ResourceRequirements"></a>
The type and amount of a resource to assign to a container. The only supported resource is a GPU.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails.md) objects
Required: No

 ** Secrets **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Secrets"></a>
The secrets to pass to the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails.md) objects
Required: No

 ** StartTimeout **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-StartTimeout"></a>
The number of seconds to wait before giving up on resolving dependencies for a container.
Type: Integer
Required: No

 ** StopTimeout **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-StopTimeout"></a>
The number of seconds to wait before the container is stopped if it doesn't shut down normally on its own.
Type: Integer
Required: No

 ** SystemControls **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-SystemControls"></a>
A list of namespaced kernel parameters to set in the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails.md) objects
Required: No

 ** Ulimits **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-Ulimits"></a>
A list of ulimits to set in the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails.md) objects
Required: No

 ** User **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-User"></a>
The user to use inside the container.
The value can use one of the following formats.
+  ` user `
+  ` user `:` group `
+  ` uid `
+  ` uid `:` gid `
+  ` user `:` gid `
+  ` uid `:` group `
Type: String
Pattern: `.*\S.*`
Required: No

 ** VolumesFrom **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-VolumesFrom"></a>
Data volumes to mount from another container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails](API_AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails.md) objects
Required: No

 ** WorkingDirectory **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDetails-WorkingDirectory"></a>
The working directory in which to run commands inside the container.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
