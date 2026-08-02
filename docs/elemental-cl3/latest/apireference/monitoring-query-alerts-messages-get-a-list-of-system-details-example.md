---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-system-details-example.html
---

# Example
<a name="monitoring-query-alerts-messages-get-a-list-of-system-details-example"></a>

```
GET http://198.51.100.0/system_info
---------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<?xml version="1.0" encoding="UTF-8"?>
<hash>
  <serial-number>None</serial-number>
  <cpu-info type="array">
    <cpu-info>
      <model>Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz</model>
      <count type="integer">8</count>
    </cpu-info>
  </cpu-info>
  <cpu-summary>8x Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz</cpu-summary>
  <mem-info>
    <total type="integer">8254267392</total>
    <used type="integer">5460201472</used>
    <free type="integer">2794065920</free>
    <shared type="integer">0</shared>
    <buffers type="integer">457605120</buffers>
    <cached type="integer">2555064320</cached>
  </mem-info>
  <network-info type="array">
    <network-info>02:00.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)</network-info>
    <network-info>02:01.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)</network-info>
    <network-info>02:02.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01)</network-info>
  </network-info>
  <md-raid>
  </md-raid>
  <hardware-raid type="array"/>
  <mount-info type="array">
    <mount-info>
      <device>sda1</device>
      <path>/boot</path>
      <size type="integer">101529600</size>
      <used type="integer">35848192</used>
      <avail type="integer">60438528</avail>
      <percent type="integer">38</percent>
    </mount-info>
    <mount-info>
      <device>VolGroup00-LogVol00</device>
      <path>/</path>
      <size type="integer">20609396736</size>
      <used type="integer">3405201408</used>
      <avail type="integer">16157298688</avail>
      <percent type="integer">18</percent>
    </mount-info>
    <mount-info>
      <device>VolGroup00-LogVol02</device>
      <path>/opt</path>
      <size type="integer">5284429824</size>
      <used type="integer">1384677376</used>
      <avail type="integer">3631316992</avail>
      <percent type="integer">28</percent>
    </mount-info>
    <mount-info>
      <device>VolGroup00-LogVol03</device>
      <path>/var/lib/mysql</path>
      <size type="integer">10568916992</size>
      <used type="integer">179785728</used>
      <avail type="integer">9852260352</avail>
      <percent type="integer">2</percent>
    </mount-info>
    <mount-info>
      <device>VolGroup00-LogVol04</device>
      <path>/data</path>
      <size type="integer">62488891392</size>
      <used type="integer">7324286976</used>
      <avail type="integer">51990355968</avail>
      <percent type="integer">13</percent>
    </mount-info>
    <mount-info>
      <path>total</path>
      <size type="integer">99053164544</size>
      <used type="integer">12329799680</used>
      <avail type="integer">81691670528</avail>
      <percent type="integer">14</percent>
    </mount-info>
  </mount-info>
</hash>
```
