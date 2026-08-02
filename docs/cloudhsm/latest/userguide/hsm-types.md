---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-types.html
---

# HSM types in AWS CloudHSM
<a name="hsm-types"></a>

AWS CloudHSM also offers two hardware security module (HSM) types: *hsm1.medium* and *hsm2m.medium*. Review the details on this page before deciding which HSM type is right for your needs.

In addition to cluster modes, AWS CloudHSM offers two HSM types: *hsm1.medium* and *hsm2m.medium*. Each HSM type uses different hardware, and each cluster can only contain one type of HSM. The following table lists the major differences between the two:

<table>
<thead>
  <tr><th>Differentiating feature</th><th>hsm1.medium</th><th>hsm2m.medium</th></tr>
</thead>
<tbody>
  <tr><td>**Cluster mode compatibility**</td><td>Available for clusters in FIPS mode.</td><td>Available for clusters in FIPS or non-FIPS mode.</td></tr>
  <tr><td>**Network type compatibility**</td><td>Not available</td><td>Available for clusters in FIPS or non-FIPS mode.</td></tr>
  <tr><td>**Backup compatibility**</td><td>Can be used to backup and restore to **hsm1.medium** and **hsm2m.medium** clusters in FIPS mode.</td><td>Can only be used to backup and restore **hsm2m.medium** clusters.</td></tr>
  <tr><td>**Key capacity**</td><td>3,300 per cluster.</td><td>16,666 total keys, with asymmetric keys having a maximum of 3,333 per cluster.</td></tr>
  <tr><td>**[Client SDKs](use-hsm.md)**</td><td>Supports all Client SDKs.</td><td>Supports all Client SDKs.</td></tr>
  <tr><td>**[Client SDK versions](client-history.md)**</td><td>Compatible with SDK version 3.1.0 and later.</td><td>Compatible with Client SDK version 5.9.0 and later.</td></tr>
  <tr><td>**Region availability **</td><td>CloudHSM no longer supports creating new clusters in any AWS Region. For more information, see [Deprecation notifications](compliance-dep-notif.md#hsm-dep-1) for details.</td><td>Available in AWS Regions that [CloudHSM is available.](https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html)</td></tr>
  <tr><td>**Performance**</td><td colspan="2">To see the performance of each HSM type, refer to [AWS CloudHSM performance information](performance.md).</td></tr>
  <tr><td>**Certification**</td><td>FIPS 140-2, PCI DSS, PCI PIN, SOC2, and PCI-3DS compliant.</td><td>FIPS 140-3, PCI DSS, PCI PIN, SOC2 and PCI-3DS compliant.</td></tr>
</tbody>
</table>
