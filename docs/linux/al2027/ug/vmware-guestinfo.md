---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/vmware-guestinfo.html
---

# VMware guestinfo `cloud-init` configuration for AL2027 on VMware
<a name="vmware-guestinfo"></a>

 VMware environments do not have the [Amazon EC2 Instance Metadata Service (IMDS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service), so an alternate method of configuring AL2027 is required. This section describes how to use an alternative configuration mechanism to the `seed.iso` virtual CD-ROM drive that is available in VMware vSphere.

 This method of configuration uses the VMware `extraconfig` mechanism to provide configuration data to `cloud-init`. For each of the following keys, a corresponding **{{keyname}}.encoding** property must be provided.

 The following keys can be provided to the VMware `extraconfig` mechanism.

** `guestinfo.metadata` **
 JSON or YAML containing `cloud-init` meta-data

** `guestinfo.userdata` **
 A YAML document containing `cloud-init` user-data in the `cloud-config` format.

** `guestinfo.vendordata` (optional) **
 YAML containing `cloud-init` vendor-data

 The corresponding encoding properties ( `guestinfo.metadata.encoding`, `guestinfo.userdata.encoding`, and `guestinfo.vendordata.encoding`) can contain:

** `base64` **
 The content of the property is `base64` encoded.

** `gzip+base64` **
 The content of the property is compressed with `gzip` after `base64` encoding.

**Note**
 The `seed.iso` method supports a separate (optional) `network-config` configuration file. VMware `guestinfo` differs in how the networking configuration is provided. See the following section for details.

 To use an explicit network configuration, embed it in the `metadata` as two YAML or JSON properties:

** `network` **
 Contains the encoded network configuration in JSON or YAML form.

** `network.encoding` **
 Contains the encoding of the above network configuration data. The `cloud-init` supported encodings are the same as for the `guestinfo` data: `base64` and `gzip+base64`.

**Example Using the VMware vSphere **govc** CLI tool to pass configuration with `guestinfo`**

1.  Prepare the `meta-data`, `user-data`, and optional `network-config` configuration files as described in [NoCloud (`seed.iso`) `cloud-init` configuration for Amazon Linux 2027 on KVM and VMware](seed-iso.md).

1.  Convert the configuration files into formats usable by VMware `guestinfo`.

   ```
   # 'meta-data', `user-data` and `network-config` are the configuration
   # files in the same format that would be used by a NoCloud (seed.iso)
   # data source, read-them and convert them to VMware guestinfo
   #
   # The VM_NAME variable is assumed to be set to the name of the VM
   # It is assumed that the necessary govc environment (credentials etc...) are already set

   metadata=$(cat "meta-data")
   userdata=$(cat "user-data")
   if [ -e "network-config" ] ; then
       # We need to embed the network config inside the meta-data
       netconf=$(base64 -w0 "network-config")
       metadata=$(printf "%s\nnetwork: %s\nnetwork.encoding: base64" "$metadata" "$netconf")
   fi
   metadata=$(base64 -w0 <<< "$metadata")
   govc vm.change -vm "$VM_NAME" \
       -e guestinfo.metadata="$metadata" \
       -e guestinfo.metadata.encoding="base64"
   userdata=$(base64 -w0 <<< "$userdata")
   govc vm.change -vm "$VM_NAME" \
       -e guestinfo.userdata="$userdata" \
       -e guestinfo.userdata.encoding="base64"
   ```
