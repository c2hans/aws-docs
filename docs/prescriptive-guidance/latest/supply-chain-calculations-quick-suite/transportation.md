---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/supply-chain-calculations-quick-suite/transportation.html
---

# Transportation
<a name="transportation"></a>

*Transportation* is the function of planning, scheduling, and controlling the activities surrounding mode, vendor, and movement of inventory into and out of an organization. Transportation includes the actual movement of the product. Many transportation teams incorporate capabilities such as in-transit storage, documentation, diversion and reconsignment services, loading and unloading, terminal and freight services, and other value-added services.

Transportation modes typically include the following:
+ Truckload
+ Less than truckload
+ Rail
+ Air
+ Ocean
+ Pipeline
+ Intermodal
+ Parcel, carrier, or express

The stakeholders of transporting inventory typically include the following:
+ The shipper
+ The recipient
+ Carriers and agents
+ The government
+ The public

## Inbound transportation
<a name="inbound-transportation"></a>

*Inbound transportation* is the logistics and cost of bringing finished goods, supplies, or materials into the business. For inbound transportation, the business is the recipient. The following table contains calculations you can use to assess inbound transportation for your supply chain.

**Note**
All of the calculations in this table are intended to evaluate the supply chain for a specific period of time that you define. For example, you could use these calculations to evaluate costs and throughput on a quarterly or yearly basis, for either a fiscal year or a calendar year.

|
|
| Name | Description | Calculation |
| --- |--- |--- |
| Percent of inbound transportation cost per receipt | This calculates the value of the inbound receipts to the total inbound transportation costs. | `Total inbound receipt value / Total inbound transportation cost` |
| Percent of inbound freight by carrier | This calculates the percentage of inbound freight handled by a specific carrier. | `# of inbound shipments for a specific carrier / Total inbound shipments` |
| Percent of inbound freight by mode | This calculates the percentage of the inbound freight delivered by a specific transportation mode. | `# shipments for a specific transport mode / Total inbound shipments` |
| Percent of inbound freight by origin | This calculates the percentage of the inbound freight from a specific origin, such as country or a supplier. | `# of shipments from a specific origin / Total inbound shipments` |
| Percent of inbound transportation costs by department | This calculates the percentage of the inbound transportation costs for a department, as assigned to the product. | `Inbound transportation costs for a specific department / Total inbound transportation costs` |
| Percent of inbound shipment acceptance | This calculates the percentage of inbound shipments accepted for a committed carrier. A *committed carrier* is a confirmed, contracted partner for specific shipment lanes. | `# of accepted inbound shipments / Total inbound shipments` |
| Percent of committed lane shipments compared to random shipments | The calculation compares committed lane shipments to random shipments. | `Total random shipments / # of committed lane shipments` |
| Accessorial changes as percent of total freight | This calculates the percent of freight costs that are due to accessorial charges. *Accessorial charges* and *surcharges* are fees charged by the carrier for services beyond standard delivery, such as trailer detention or demurrage, redelivery, or fuel increases. Often, these are extra costs incurred due to inefficient processes. | `(Accessorial charges + surcharges) / Total freight` |
| Average inbound cubic volume per shipment for a specific route | This calculates the average cubic volume, such as cubic feet or cubic meters, of inbound shipments for a specific route. | `Total cubic volume shipped by route / # of shipments by route` |
| Average inbound distance traveled per shipment | This calculates the average distance traveled for each inbound shipment. | `Total inbound distance traveled / # of shipments` |
| Average inbound rate per mile or kilometer | This calculates the average inbound rate for each mile or kilometer traveled. You can run this calculation for all transportation modes or for a specific mode, such as truckload, rail, air, or ocean. | `Total inbound rate charged / Total inbound distance traveled` |
| Average inbound transportation cost per shipment | This calculates the average inbound transportation cost for each shipment. | `Total inbound transportation cost / # of inbound shipments` |
| Average inbound transportation cost per shipment by transportation mode | This calculates the average inbound transportation cost for each shipment sent by a specific inbound transportation mode, for inbound product flow. Transportation modes can include truckload, less than truckload, rail, ocean, and intermodal. | `Total inbound transportation cost for the mode / # of inbound shipments for the mode` |
| Average inbound transportation cost per case | This calculates the average inbound transportation cost for each case shipped. | `Total inbound transportation cost / Total inbound cases shipped` |
| Average inbound transportation cost per cubic unit | This calculates the average inbound transportation cost for each cubic unit of measure, such as a cubic foot or cubic meter. | `Total inbound transportation cost / Total inbound cubic volume shipped` |
| Average inbound transportation cost by value of shipped materials | This calculates the average inbound transportation cost for each monetary unit of value, such as a dollar, of goods and materials shipped. | `Total inbound transportation cost / Total inbound value shipped` |
| Average inbound transportation cost per mile or kilometer | This calculates the average inbound transportation cost for each mile or kilometer traveled. | `Total inbound transportation cost / Total inbound distance traveled` |
| Average inbound transportation cost per pallet | This calculates the average inbound transportation cost for each pallet shipped. | `Total inbound transportation cost / Total inbound pallets shipped` |
| Average inbound transportation cost per purchase order | This calculates the average inbound transportation cost for each purchase order. | `Total inbound transportation cost / Total inbound purchase orders shipped` |
| Average inbound transportation cost per SKU or item | This calculates the average inbound transportation cost for each SKU or item shipped. | `Total inbound transportation cost / Total inbound SKUs shipped` |
| Average inbound transportation cost per store | This calculates the average inbound transportation cost for each store serviced. | `Total inbound transportation cost / Total store count` |
| Average inbound transportation cost per units shipped | This calculates the average inbound transportation cost for each unit shipped. | `Total inbound transportation cost / Total inbound units shipped` |
| Average inbound transportation cost by weight | This calculates the average inbound transportation cost for each unit of weight, such as a pound or kilogram, shipped. | `Total inbound transportation cost / Total inbound weight shipped` |
| Average weight of inbound shipments | This calculates the average weight, in pounds or kilograms, of inbound shipments. | `Total inbound weight shipped / Total number of inbound shipments` |
| Percent of inbound shipments with consolidations | This calculates the percent of inbound shipments that have consolidations. *Consolidation* is the process of combining multiple shipments into a single container, to reduce transportation costs. Shipments can be combined to make multiple deliveries in a particular geographic region, or they can be consolidated to make a single delivery to a single recipient. | `# of inbound shipments with consolidations / Total inbound shipments` |
| Inbound freight costs as percentage of purchases | Calculated by dividing inbound freight costs by purchase value. It is important to understand the underlying detail. The measurement can vary widely, depending on whether raw materials are purchased on a delivered, prepaid, or collect basis. | `Total inbound freight costs / Net sales` |
| Percent of inbound shipments that arrived on time | This calculates the percentage of inbound shipments that were received within the delivery window specified on the purchase order. | `Total inbound orders received on time / # of inbound orders` |
| Percent of weight capacity utilized for inbound shipments | This calculation is generally used for shipments over a specified weight, such as 10,000 pounds. This calculates the percentage of inbound weight capacity used.<br />For example, assume you have 1 truck that has a weight capacity of 40,000 pounds. If you received 675 shipments with that truck, the total weight capacity was 27 million pounds. However, if you received only 22.95 million pounds of product, then you used 85% of the weight capacity. The 15% unused capacity is an opportunity for more efficiency. | `Total inbound weight shipped / Total inbound weight capacity` |
| Percent of inbound shipments that offer tracking | This calculates the percentage of inbound shipments that were sent through a carrier that offers tracking information. Tracking information provides visibility and helps you trace the shipment. This metric is an indicator of the relative sophistication of your carrier base, and it's one measure of the non-price value available from your carrier base. | `# of inbound shipments sent through carriers that offer tracking / Total number of inbound shipments` |

## Outbound transportation
<a name="outbound-transportation"></a>

*Outbound transportation* is the logistics and cost of moving finished goods and products to end recipients, such as customers. Outbound transportation focuses on delivery rather than receipt. The following table contains calculations you can use to assess outbound transportation for your supply chain.

**Note**
All of the calculations in this table are intended to evaluate the supply chain for a specific period of time that you define. For example, you could use these calculations to evaluate costs and throughput on a quarterly or yearly basis, for either a fiscal year or a calendar year.

|
|
| Name | Description | Calculation |
| --- |--- |--- |
| Total outbound transportation distance (also known as *distance run*) | This calculates the total outbound transportation distance, in miles or kilometers. | `Sum(outbound transportation distance of all shipments)` |
| Percent of outbound freight by carrier | This calculates the percentage of the outbound freight handled by a specific carrier. | `# of outbound shipments for a specific carrier / Total outbound shipments ` |
| Percent of outbound freight by mode | This calculates the percentage of the outbound freight by shipped by a specific transportation mode. | `# outbound shipments for a specific transport mode / Total outbound shipments ` |
| Percent of outbound transportation cost by department | This calculates the percentage of the outbound transportation costs for a department, as assigned to the product. | `Outbound transportation cost for a specific department / Total outbound transportation cost` |
| Average number of stops per outbound shipment | This calculates the average number of stops the trucks make on their route. | `Total stops / # of shipments` |
| Average cubic volume per outbound shipment for a specific route | This calculates the average cubic volume, such as cubic feet or cubic meters, of outbound shipments for a specific route. | `Total cubic volume shipped by route / Total # of shipments by route` |
| Average distance traveled per outbound shipment | This calculates the average distance traveled for each outbound shipment. | `Total distance traveled / # of shipments` |
| Average outbound rate per mile or kilometer | This calculates the average outbound rate for each mile or kilometer traveled. You can run this calculation for all transportation modes or for a specific mode, such as truckload, rail, air, or ocean. | `Total outbound rate charged / Total outbound distance traveled` |
| Average outbound transportation cost per shipment | This calculates the average outbound transportation cost for each shipment. | `Total outbound transportation cost / # of outbound shipments` |
| Average outbound transportation cost per shipment by transportation mode | This calculates the average outbound transportation cost for each shipment by transportation mode, for outbound product flow. Transportation modes can include truckload, less than truckload, rail, ocean, and intermodal. | `Total outbound transportation cost for the mode / # of outbound shipments for the mode` |
| Average outbound transportation cost per case | This calculates the average outbound transportation cost for each case shipped. | `Total outbound transportation cost / Total outbound cases shipped` |
| Average outbound transportation cost per cubic unit | This calculates the average outbound transportation cost for each cubic unit of measure, such as a cubic foot or cubic meter. | `Total outbound transportation cost / Total outbound cubic volume shipped` |
| Average outbound transportation cost by value of shipped goods | This calculates the average outbound transportation cost for each monetary unit of value, such as a dollar, of goods shipped. | `Total outbound transportation cost / Total outbound value shipped` |
| Average outbound transportation cost per mile or kilometer | This calculates the average outbound transportation cost for each mile or kilometer traveled. | `Total outbound transportation cost / Total outbound distance traveled` |
| Average outbound transportation cost per pallet | This calculates the average outbound transportation cost for each pallet shipped. | `Total outbound transportation cost / Total outbound pallets shipped` |
| Average outbound transportation cost per purchase order | This calculates the average outbound transportation cost for each purchase order. | `Total outbound transportation cost / Total outbound purchase orders shipped` |
| Average outbound transportation cost per SKU or item | This calculates the average outbound transportation cost for each SKU or item shipped. | `Total outbound transportation cost / Total outbound SKUs shipped` |
| Average outbound transportation cost per store | This calculates the average outbound transportation cost for each store serviced. | `Total outbound transportation cost / Total store count` |
| Average outbound transportation cost per unit shipped | This calculates the average outbound transportation cost for each unit shipped. | `Total outbound transportation cost / Total outbound units shipped` |
| Average outbound transportation cost by weight | This calculates the average inbound transportation cost for each unit of weight, such as a pound or kilogram, shipped. | `Total outbound transportation cost / Total outbound weight shipped` |
| Average weight of outbound shipments | This calculates the average weight, in pounds or kilograms, of outbound shipments. | `Total outbound weight shipped / Total number of outbound shipments` |

## Total and overall transportation
<a name="overall-transportation"></a>

The following table contains calculations you can use to assess overall transportation for your supply chain, including inbound and outbound transportation.

**Note**
All of the calculations in this table are intended to evaluate the supply chain for a specific period of time that you define. For example, you could use these calculations to evaluate costs and throughput on a quarterly or yearly basis, for either a fiscal year or a calendar year.

|
|
| Name | Description | Calculation |
| --- |--- |--- |
| Percent of freight by carrier | This calculates the percentage of freight handled by a specific carrier. | `# of shipments for a specific carrier / Total shipments` |
| Percent of freight by mode | This calculates the percentage of freight delivered by a specific transportation mode. | `# shipments for a specific transport mode / Total shipments` |
| Percent of transportation cost by department | This calculates the percentage of transportation costs for a department, as assigned to the product. | `Transportation cost for a specific department / Total shipments` |
| Average cubic volume per shipment for a specific route | This calculates the average cubic volume, such as cubic feet or cubic meters, of shipments for a specific route. | `Total cubic volume shipped by route / Total # of shipments by route` |
| Average distance traveled per shipment | This calculates the average distance traveled for each shipment. | `Total distance traveled / # of shipments` |
| Average rate per mile or kilometer | This calculates the average rate for each mile or kilometer traveled. | `Total rate charged / Total distance traveled` |
| Average rate per mile or kilometer by transportation mode | This calculates the average rate for each mile or kilometer traveled by a specific transportation mode. | `Total rate charged by mode / Total distance traveled by mode` |
| Average SKU count per shipment | This calculates the average number of unique items (SKUs) in each shipment. | `# of unique SKUs shipped / # of shipments` |
| Average transportation cost per shipment | This calculates the average transportation cost for each shipment. | `Total transportation cost / # of shipments` |
| Average transportation cost per shipment by transportation mode | This calculates the average transportation cost for each shipment by transportation mode. Transportation modes can include truckload, less than truckload, rail, ocean, and intermodal. | `Total transportation cost by mode / # of shipments by mode` |
| Average transportation cost per case | This calculates the average transportation cost for each case shipped. | `Total transportation cost / Total cases shipped` |
| Average transportation cost per cubic unit | This calculates the average transportation cost for each cubic unit of measure, such as a cubic foot or cubic meter. | `Total transportation cost / Total cubic volume shipped` |
| Average transportation cost by shipped goods value | This calculates the average transportation cost for each monetary unit of value, such as a dollar, of goods and materials shipped. | `Total transportation cost / Total value shipped` |
| Average transportation cost per mile or kilometer | This calculates the average transportation cost for each mile or kilometer traveled. | `Total transportation cost / Total distance traveled` |
| Average transportation cost per pallet | This calculates the average transportation cost for each pallet shipped. | `Total transportation cost / Total pallets shipped` |
| Average transportation cost per purchase order | This calculates the average transportation cost for each purchase order. | `Total transportation cost / Total purchase orders shipped` |
| Average transportation cost per SKU or item | This calculates the average transportation cost for each SKU or item shipped. | `Total transportation cost / Total SKUs shipped` |
| Average transportation cost per store | This calculates the average transportation cost for each store serviced. | `Total transportation cost / Total store count` |
| Average transportation cost per units shipped | This calculates the average inbound transportation cost for each unit shipped. | `Total transportation cost / Total units shipped` |
| Average transportation cost by weight | This calculates the average transportation cost for each unit of weight, such as a pound or kilogram, shipped. | `Total transportation cost / Total weight shipped` |
| Average weight of shipments | This calculates the average shipment weight, in pounds or kilograms. | `Total weight shipped / Total number of shipments` |
| Number of carriers per transportation mode | This calculates percentage of freight carriers for a particular transportation mode, such as truckload, rail, or ocean. This is an indication of your volume leverage and control over the transportation function. | `Total freight carriers for the transportation mode / Total freight carriers` |
| On-time pickups | This calculates the percentage of pickups that were on-time. You can run this calculation for a specific carrier or as a total of all carriers. This metric is an indication of the freight carrier's performance and effect on your shipping operations and customer service. | `# of on-time pickups / # of shipments` |
| On-time shipping rate | The *on-time shipping rate* is the percentage of times your customer receives product within the promised shipping window. Tracking this metric helps assess the efficiency of your supply chain processes. | `Number of items delivered on time / Total items shipped` |
| Percent of truckload cubic volume capacity utilized | This calculates the percentage of truck volume capacity used. For example, assume you have 1 truck that has a volume capacity of 1,800 cubic feet. If you receive 675 shipments with that truck, the total volume capacity was 1.2 cubic feet. However, if you received only 1.0 million cubic feet of product, then you used 83% of the volume capacity. The 17% unused capacity is an opportunity for more efficiency. | `Total cubic volume shipped / Total cubic volume capacity` |
| Supplier on-time delivery | This calculates the percentage of time a supplier delivers products within the agreed-on time frame. | `Number of items supplier delivered on time / Total items supplier shipped` |
| Transit time (sometimes referred to as *transit* *lead time*) | *Transit time* is the number of days or hours between when a shipment leaves your facility and arrives at the destination. Often measured against a standard transit time quoted by the carrier for each traffic lane. Unless you are integrated into your customers' systems, you have to rely on freight carriers to report their own performance. Transit time is often an important component of overall lead time. Transit times can vary substantially, based on transportation mode, carrier, and distance. | `Count(days travel time)` |
| Truck turnaround time | This calculates the average time elapsed between a truck's arrival at the facility and its departure. This is an indicator of the efficiency of the lot and dock door space, receiving processes, and shipping processes. This also directly affects freight carrier profits on the business. | `Average(truck arrival time - truck departure time)` |
