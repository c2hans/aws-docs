---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-queues.html
---

# ENA queues
<a name="ena-queues"></a>

ENA queues are allocated to network interfaces with default static limits based on the instance type and size. On supported instance types, you can dynamically allocate these queues across Elastic Network Interfaces (ENIs). While the total queue count per instance depends on its type and size, you can configure multiple ENIs with ENA queues until you meet the maximum queue count for the ENI and the instance.

Flexible ENA queue allocation optimizes resource distribution, enabling maximum vCPU utilization. High network performance workloads typically require multiple ENA queues. You can fine-tune network performance and packets per second (PPS) by adjusting queue counts according to your specific workload needs. For example, network-intensive applications may require more queues compared to CPU-intensive applications.

**Topics**
+ [Supported instances](#supported-instances)
+ [Modify the number of queues](#modify)

## Supported instances
<a name="supported-instances"></a>

The following instances support dynamic allocation of multiple ENA queues.

### General purpose
<a name="supported-instances-ena-queues-gp"></a>

<table>
<thead>
  <tr><th>Instance type</th><th>Default ENA queues per interface</th><th>Maximum ENA queues per interface</th><th>Maximum ENA queues per instance</th></tr>
</thead>
<tbody>
  <tr><td colspan="4">M6i</td></tr>
  <tr><td>m6i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m6i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m6i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m6i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m6i.8xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>m6i.12xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>m6i.16xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>m6i.24xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>m6i.32xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td colspan="4">M6id</td></tr>
  <tr><td>m6id.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m6id.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m6id.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m6id.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m6id.8xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>m6id.12xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>m6id.16xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>m6id.24xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>m6id.32xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td colspan="4">M6idn</td></tr>
  <tr><td>m6idn.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m6idn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m6idn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m6idn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m6idn.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m6idn.12xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m6idn.16xlarge</td><td>16</td><td>32</td><td>240</td></tr>
  <tr><td>m6idn.24xlarge</td><td>32</td><td>32</td><td>480</td></tr>
  <tr><td>m6idn.32xlarge</td><td>32</td><td>32</td><td>512 \*</td></tr>
  <tr><td colspan="4">M6in</td></tr>
  <tr><td>m6in.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m6in.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m6in.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m6in.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m6in.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m6in.12xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m6in.16xlarge</td><td>16</td><td>32</td><td>240</td></tr>
  <tr><td>m6in.24xlarge</td><td>32</td><td>32</td><td>480</td></tr>
  <tr><td>m6in.32xlarge</td><td>32</td><td>32</td><td>512 \*</td></tr>
  <tr><td colspan="4">M8a</td></tr>
  <tr><td>m8a.medium</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>m8a.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m8a.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8a.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8a.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8a.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m8a.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8a.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8a.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8a.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8a.metal-24xl</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8a.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td colspan="4">M8azn</td></tr>
  <tr><td>m8azn.medium</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>m8azn.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8azn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8azn.3xlarge</td><td>4</td><td>16</td><td>48</td></tr>
  <tr><td>m8azn.6xlarge</td><td>8</td><td>32</td><td>96</td></tr>
  <tr><td>m8azn.12xlarge</td><td>8</td><td>64</td><td>192</td></tr>
  <tr><td>m8azn.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8azn.metal-12xl</td><td>8</td><td>64</td><td>192</td></tr>
  <tr><td>m8azn.metal-24xl</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td colspan="4">M8gb</td></tr>
  <tr><td>m8gb.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>m8gb.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m8gb.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8gb.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8gb.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8gb.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m8gb.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8gb.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8gb.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8gb.48xlarge</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td>m8gb.metal-24xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8gb.metal-48xl</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td colspan="4">M8gn</td></tr>
  <tr><td>m8gn.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>m8gn.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m8gn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8gn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8gn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8gn.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m8gn.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8gn.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8gn.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8gn.48xlarge</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td>m8gn.metal-24xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8gn.metal-48xl</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td colspan="4">M8i</td></tr>
  <tr><td>m8i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m8i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8i.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m8i.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8i.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8i.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8i.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>m8i.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8i.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>m8i.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8i.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td colspan="4">M8id</td></tr>
  <tr><td>m8id.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m8id.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8id.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8id.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8id.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m8id.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8id.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8id.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m8id.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>m8id.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8id.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>m8id.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8id.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td colspan="4">M8i-flex</td></tr>
  <tr><td>m8i-flex.large</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>m8i-flex.xlarge</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8i-flex.2xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8i-flex.4xlarge</td><td>4</td><td>8</td><td>32</td></tr>
  <tr><td>m8i-flex.8xlarge</td><td>4</td><td>16</td><td>64</td></tr>
  <tr><td>m8i-flex.12xlarge</td><td>8</td><td>32</td><td>96</td></tr>
  <tr><td>m8i-flex.16xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td colspan="4">M8in</td></tr>
  <tr><td>m8in.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8in.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8in.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8in.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8in.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m8in.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8in.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8in.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>m8in.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>m8in.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8in.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>m8in.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8in.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">M8idn</td></tr>
  <tr><td>m8idn.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8idn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8idn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8idn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8idn.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m8idn.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8idn.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8idn.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>m8idn.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>m8idn.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8idn.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>m8idn.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8idn.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">M8ine</td></tr>
  <tr><td>m8ine.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8ine.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8ine.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8ine.4xlarge</td><td>16</td><td>16</td><td>128</td></tr>
  <tr><td>m8ine.8xlarge</td><td>32</td><td>32</td><td>256</td></tr>
  <tr><td>m8ine.12xlarge</td><td>32</td><td>64</td><td>384</td></tr>
  <tr><td colspan="4">M8ib</td></tr>
  <tr><td>m8ib.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8ib.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8ib.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8ib.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8ib.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m8ib.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8ib.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8ib.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>m8ib.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>m8ib.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8ib.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>m8ib.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8ib.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">M8idb</td></tr>
  <tr><td>m8idb.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>m8idb.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m8idb.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m8idb.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m8idb.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>m8idb.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m8idb.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m8idb.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>m8idb.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>m8idb.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8idb.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>m8idb.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m8idb.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">M9g</td></tr>
  <tr><td>m9g.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>m9g.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m9g.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m9g.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m9g.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m9g.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m9g.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m9g.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m9g.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m9g.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m9g.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td colspan="4">M9gd</td></tr>
  <tr><td>m9gd.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>m9gd.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>m9gd.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>m9gd.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>m9gd.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>m9gd.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>m9gd.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>m9gd.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>m9gd.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>m9gd.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>m9gd.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
</tbody>
</table>

**Note**
\* These instance types feature multiple network cards. Other instance types feature a single network card. For more information, see [Network cards](using-eni.md#network-cards).

### Compute optimized
<a name="supported-instances-ena-queues-co"></a>

<table>
<thead>
  <tr><th>Instance type</th><th>Default ENA queues per interface</th><th>Maximum ENA queues per interface</th><th>Maximum ENA queues per instance</th></tr>
</thead>
<tbody>
  <tr><td colspan="4">C6i</td></tr>
  <tr><td>c6i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c6i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c6i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c6i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c6i.8xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>c6i.12xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>c6i.16xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>c6i.24xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>c6i.32xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td colspan="4">C6id</td></tr>
  <tr><td>c6id.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c6id.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c6id.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c6id.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c6id.8xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>c6id.12xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>c6id.16xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>c6id.24xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>c6id.32xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td colspan="4">C6in</td></tr>
  <tr><td>c6in.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c6in.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c6in.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c6in.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c6in.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>c6in.12xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>c6in.16xlarge</td><td>16</td><td>32</td><td>240</td></tr>
  <tr><td>c6in.24xlarge</td><td>32</td><td>32</td><td>480</td></tr>
  <tr><td>c6in.32xlarge</td><td>32</td><td>32</td><td>512 \*</td></tr>
  <tr><td colspan="4">C8a</td></tr>
  <tr><td>c8a.medium</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>c8a.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c8a.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8a.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8a.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8a.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c8a.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8a.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8a.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c8a.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8a.metal-24xl</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c8a.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td colspan="4">C8gb</td></tr>
  <tr><td>c8gb.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>c8gb.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c8gb.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8gb.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8gb.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8gb.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c8gb.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8gb.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8gb.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c8gb.48xlarge</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td>c8gb.metal-24xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8gb.metal-48xl</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td colspan="4">C8gn</td></tr>
  <tr><td>c8gn.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>c8gn.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c8gn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8gn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8gn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8gn.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c8gn.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8gn.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8gn.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c8gn.48xlarge</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td>c8gn.metal-24xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8gn.metal-48xl</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td colspan="4">C8i</td></tr>
  <tr><td>c8i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c8i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8i.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c8i.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8i.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8i.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c8i.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>c8i.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8i.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>c8i.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8i.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td colspan="4">C8id</td></tr>
  <tr><td>c8id.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c8id.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8id.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8id.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8id.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c8id.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8id.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8id.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c8id.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>c8id.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8id.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>c8id.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8id.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td colspan="4">C8i-flex</td></tr>
  <tr><td>c8i-flex.large</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>c8i-flex.xlarge</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>c8i-flex.2xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8i-flex.4xlarge</td><td>4</td><td>8</td><td>32</td></tr>
  <tr><td>c8i-flex.8xlarge</td><td>4</td><td>16</td><td>64</td></tr>
  <tr><td>c8i-flex.12xlarge</td><td>8</td><td>32</td><td>96</td></tr>
  <tr><td>c8i-flex.16xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td colspan="4">C8in</td></tr>
  <tr><td>c8in.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>c8in.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8in.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8in.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8in.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>c8in.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8in.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8in.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>c8in.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>c8in.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8in.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>c8in.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8in.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">C8ine</td></tr>
  <tr><td>c8ine.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>c8ine.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8ine.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8ine.4xlarge</td><td>16</td><td>16</td><td>128</td></tr>
  <tr><td>c8ine.8xlarge</td><td>32</td><td>32</td><td>256</td></tr>
  <tr><td>c8ine.12xlarge</td><td>32</td><td>64</td><td>384</td></tr>
  <tr><td colspan="4">C8ib</td></tr>
  <tr><td>c8ib.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>c8ib.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c8ib.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c8ib.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c8ib.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>c8ib.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c8ib.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c8ib.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>c8ib.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>c8ib.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8ib.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>c8ib.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c8ib.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">C9g</td></tr>
  <tr><td>c9g.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>c9g.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c9g.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c9g.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c9g.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c9g.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c9g.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c9g.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c9g.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c9g.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c9g.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td colspan="4">C9gd</td></tr>
  <tr><td>c9gd.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>c9gd.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>c9gd.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>c9gd.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>c9gd.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>c9gd.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>c9gd.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>c9gd.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>c9gd.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>c9gd.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>c9gd.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
</tbody>
</table>

**Note**
\* These instance types feature multiple network cards. Other instance types feature a single network card. For more information, see [Network cards](using-eni.md#network-cards).

### Memory optimized
<a name="supported-instances-ena-queues-mo"></a>

<table>
<thead>
  <tr><th>Instance type</th><th>Default ENA queues per interface</th><th>Maximum ENA queues per interface</th><th>Maximum ENA queues per instance</th></tr>
</thead>
<tbody>
  <tr><td colspan="4">R6i</td></tr>
  <tr><td>r6i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r6i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r6i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r6i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r6i.8xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>r6i.12xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>r6i.16xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>r6i.24xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>r6i.32xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td colspan="4">R6id</td></tr>
  <tr><td>r6id.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r6id.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r6id.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r6id.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r6id.8xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>r6id.12xlarge</td><td>8</td><td>32</td><td>64</td></tr>
  <tr><td>r6id.16xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>r6id.24xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td>r6id.32xlarge</td><td>8</td><td>32</td><td>120</td></tr>
  <tr><td colspan="4">R6idn</td></tr>
  <tr><td>r6idn.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r6idn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r6idn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r6idn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r6idn.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r6idn.12xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r6idn.16xlarge</td><td>16</td><td>32</td><td>240</td></tr>
  <tr><td>r6idn.24xlarge</td><td>32</td><td>32</td><td>480</td></tr>
  <tr><td>r6idn.32xlarge</td><td>32</td><td>32</td><td>512 \*</td></tr>
  <tr><td colspan="4">R6in</td></tr>
  <tr><td>r6in.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r6in.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r6in.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r6in.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r6in.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r6in.12xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r6in.16xlarge</td><td>16</td><td>32</td><td>240</td></tr>
  <tr><td>r6in.24xlarge</td><td>32</td><td>32</td><td>480</td></tr>
  <tr><td>r6in.32xlarge</td><td>32</td><td>32</td><td>512 \*</td></tr>
  <tr><td colspan="4">R8a</td></tr>
  <tr><td>r8a.medium</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>r8a.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r8a.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8a.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8a.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8a.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>r8a.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8a.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8a.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>r8a.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8a.metal-24xl</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>r8a.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td colspan="4">R8gb</td></tr>
  <tr><td>r8gb.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>r8gb.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r8gb.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8gb.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8gb.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8gb.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>r8gb.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8gb.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8gb.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>r8gb.48xlarge</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td>r8gb.metal-24xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8gb.metal-48xl</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td colspan="4">R8gn</td></tr>
  <tr><td>r8gn.medium</td><td>1</td><td>1</td><td>2</td></tr>
  <tr><td>r8gn.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r8gn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8gn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8gn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8gn.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>r8gn.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8gn.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8gn.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>r8gn.48xlarge</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td>r8gn.metal-24xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8gn.metal-48xl</td><td>32</td><td>128</td><td>768 \*</td></tr>
  <tr><td colspan="4">R8i</td></tr>
  <tr><td>r8i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r8i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8i.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>r8i.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8i.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8i.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>r8i.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>r8i.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8i.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>r8i.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8i.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td colspan="4">R8id</td></tr>
  <tr><td>r8id.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>r8id.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8id.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8id.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8id.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>r8id.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8id.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8id.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>r8id.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>r8id.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8id.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>r8id.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8id.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td colspan="4">R8i-flex</td></tr>
  <tr><td>r8i-flex.large</td><td>1</td><td>1</td><td>3</td></tr>
  <tr><td>r8i-flex.xlarge</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>r8i-flex.2xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8i-flex.4xlarge</td><td>4</td><td>8</td><td>32</td></tr>
  <tr><td>r8i-flex.8xlarge</td><td>4</td><td>16</td><td>64</td></tr>
  <tr><td>r8i-flex.12xlarge</td><td>8</td><td>32</td><td>96</td></tr>
  <tr><td>r8i-flex.16xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td colspan="4">R8in</td></tr>
  <tr><td>r8in.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>r8in.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8in.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8in.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8in.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r8in.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8in.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8in.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>r8in.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>r8in.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8in.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>r8in.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8in.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">R8idn</td></tr>
  <tr><td>r8idn.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>r8idn.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8idn.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8idn.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8idn.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r8idn.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8idn.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8idn.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>r8idn.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>r8idn.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8idn.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>r8idn.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8idn.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">R8ib</td></tr>
  <tr><td>r8ib.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>r8ib.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8ib.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8ib.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8ib.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r8ib.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8ib.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8ib.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>r8ib.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>r8ib.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8ib.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>r8ib.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8ib.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">R8idb</td></tr>
  <tr><td>r8idb.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>r8idb.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>r8idb.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>r8idb.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>r8idb.8xlarge</td><td>16</td><td>32</td><td>128</td></tr>
  <tr><td>r8idb.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>r8idb.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>r8idb.24xlarge</td><td>16</td><td>128</td><td>256</td></tr>
  <tr><td>r8idb.32xlarge</td><td>32</td><td>128</td><td>512</td></tr>
  <tr><td>r8idb.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8idb.96xlarge</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td>r8idb.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>r8idb.metal-96xl</td><td>32</td><td>128</td><td>1536 \*</td></tr>
  <tr><td colspan="4">X8aedz</td></tr>
  <tr><td>x8aedz.large</td><td>2</td><td>2</td><td>8</td></tr>
  <tr><td>x8aedz.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>x8aedz.3xlarge</td><td>4</td><td>16</td><td>48</td></tr>
  <tr><td>x8aedz.6xlarge</td><td>8</td><td>32</td><td>96</td></tr>
  <tr><td>x8aedz.12xlarge</td><td>8</td><td>64</td><td>192</td></tr>
  <tr><td>x8aedz.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>x8aedz.metal-12xl</td><td>8</td><td>64</td><td>192</td></tr>
  <tr><td>x8aedz.metal-24xl</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td colspan="4">X8i</td></tr>
  <tr><td>x8i.large</td><td>2</td><td>2</td><td>6</td></tr>
  <tr><td>x8i.xlarge</td><td>4</td><td>4</td><td>16</td></tr>
  <tr><td>x8i.2xlarge</td><td>8</td><td>8</td><td>32</td></tr>
  <tr><td>x8i.4xlarge</td><td>8</td><td>16</td><td>64</td></tr>
  <tr><td>x8i.8xlarge</td><td>8</td><td>32</td><td>128</td></tr>
  <tr><td>x8i.12xlarge</td><td>16</td><td>64</td><td>192</td></tr>
  <tr><td>x8i.16xlarge</td><td>16</td><td>64</td><td>256</td></tr>
  <tr><td>x8i.24xlarge</td><td>16</td><td>128</td><td>384</td></tr>
  <tr><td>x8i.32xlarge</td><td>16</td><td>128</td><td>512</td></tr>
  <tr><td>x8i.48xlarge</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>x8i.64xlarge</td><td>32</td><td>128</td><td>1024</td></tr>
  <tr><td>x8i.96xlarge</td><td>32</td><td>128</td><td>1536</td></tr>
  <tr><td>x8i.metal-48xl</td><td>32</td><td>128</td><td>768</td></tr>
  <tr><td>x8i.metal-96xl</td><td>32</td><td>128</td><td>1536</td></tr>
</tbody>
</table>

**Note**
\* These instance types feature multiple network cards. Other instance types feature a single network card. For more information, see [Network cards](using-eni.md#network-cards).

## Modify the number of queues
<a name="modify"></a>

You can modify the number of ENA queues using the AWS Management Console, AWS CLI, or PowerShell. In the AWS Management Console, the ENA queues configuration is available under each **Network interface** setting.

**Note**
Your instance must be stopped before modifying the number of ENA queues.
The value for ENA queues must be a power of 2, such as, 1, 2, 4, 8, 16, 32, etc.
The number of queues allocated to any single ENI cannot exceed the number of vCPUs available on your instance.

Before modifying the queue count, use the following command to check your current queue count.

------
#### [ AWS CLI ]

```
aws ec2 describe-instances --instance-id {{i-1234567890abcdef0}}
```

------
#### [ PowerShell ]

```
(Get-EC2Instance -InstanceId i-{{1234567890abcdef0}}).Instances.NetworkInterfaces |
  Select-Object NetworkInterfaceId,
    @{N='DeviceIndex';E={$_.Attachment.DeviceIndex}},
    @{N='AttachmentId';E={$_.Attachment.AttachmentId}},
    @{N='EnaQueueCount';E={$_.Attachment.EnaQueueCount}}
```

------

### Attach a network interface with ENA queues
<a name="modify-attach"></a>

In the following example, 16 ENA queues are configured on an ENI.

------
#### [ AWS CLI ]

**To attach a network interface with ENA queues**
Use the [attach-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-network-interface.html) command.

```
aws ec2 attach-network-interface \
  --network-interface-id eni-{{abcdef01234567890}} \
  --instance-id {{i-1234567890abcdef0}} \
  --device-index 1 \
  --ena-queue-count 16
```

------
#### [ PowerShell ]

**To attach a network interface with ENA queues**
Use the [Add-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2NetworkInterface.html) cmdlet.

```
Add-EC2NetworkInterface `
  -NetworkInterfaceId eni-{{abcdef01234567890}} `
  -InstanceId {{i-1234567890abcdef0}} `
  -DeviceIndex 1 `
  -EnaQueueCount 16
```

------

### Launch an instance with ENA queues
<a name="modify-run"></a>

In the following example, 16 ENA queues each are configured on 3 ENIs.

------
#### [ AWS CLI ]

**To launch an instance with ENA queues**
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command.

```
aws ec2 run-instances \
  --image-id ami-{{1234567890abcdef0}} \
  --instance-type c8i.4xlarge \
  --network-interfaces \
    "[{\"DeviceIndex\":0,\"SubnetId\":\"subnet-{{abcdef01234567890}}\",\"EnaQueueCount\":16},
      {\"DeviceIndex\":1,\"SubnetId\":\"subnet-{{abcdef01234567890}}\",\"EnaQueueCount\":16},
      {\"DeviceIndex\":2,\"SubnetId\":\"subnet-{{abcdef01234567890}}\",\"EnaQueueCount\":16}]"
```

------
#### [ PowerShell ]

**To launch an instance with ENA queues**
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet.

```
New-EC2Instance `
  -ImageId ami-{{1234567890abcdef0}} `
  -InstanceType c8i.4xlarge `
  -NetworkInterface @(
    @{DeviceIndex=0; SubnetId="subnet-{{abcdef01234567890}}"; EnaQueueCount=16},
    @{DeviceIndex=1; SubnetId="subnet-{{abcdef01234567890}}"; EnaQueueCount=16},
    @{DeviceIndex=2; SubnetId="subnet-{{abcdef01234567890}}"; EnaQueueCount=16}
  )
```

------

### Modify ENA queues on an existing network interface
<a name="modify-eni-attribute"></a>

In the following example, 16 ENA queues are configured on an ENI.

------
#### [ AWS CLI ]

**To modify ENA queues on a network interface**
Use the [modify-network-interface-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-network-interface-attribute.html) command.

```
aws ec2 modify-network-interface-attribute \
  --network-interface-id eni-{{1234567890abcdef0}} \
  --attachment AttachmentId=eni-attach-{{1234567890abcdef0}},EnaQueueCount=16
```

------
#### [ PowerShell ]

**To modify ENA queues on a network interface**
Use the [Edit-EC2NetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.html) cmdlet.

```
Edit-EC2NetworkInterfaceAttribute `
  -NetworkInterfaceId eni-{{1234567890abcdef0}} `
  -Attachment_AttachmentId eni-attach-{{1234567890abcdef0}} `
  -Attachment_EnaQueueCount 16
```

------

In the following example, the ENA count is reset to the default value.

------
#### [ AWS CLI ]

```
aws ec2 modify-network-interface-attribute \
  --network-interface-id eni-{{1234567890abcdef0}} \
  --attachment AttachmentId=eni-attach-{{1234567890abcdef0}},DefaultEnaQueueCount=true
```

------
#### [ PowerShell ]

```
Edit-EC2NetworkInterfaceAttribute `
  -NetworkInterfaceId eni-{{1234567890abcdef0}} `
  -Attachment_AttachmentId eni-attach-{{1234567890abcdef0}} `
  -Attachment_DefaultEnaQueueCount $true
```

------
