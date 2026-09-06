---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-workload-assessment/use-cases.html
---

# Use cases
<a name="use-cases"></a>

|
|
| Question | Example response |
| --- |--- |
| What is the primary goal or success criteria of the use case? | To improve customer support response time, increase sales conversions, enhance product recommendations. Also improve user satisfaction, task completion rate, response quality,  and so on. |
| How does this use case align with your organization's strategic goals? | This aligns with our strategic goal of enhancing customer satisfaction by reducing response times in customer service. |
| What is the expected volume of data or requests for the use case? | 500 transactions per second (TPS). |
| What types of data sources are required to support your generative AI workloads? | Internal structured databases (customer records, sales data, and so on); unstructured text data from documents, emails, and social media; audio and video files for speech and image recognition tasks; real-time streaming data from IoT devices and sensors; public datasets and APIs for enrichment. |
| How frequently do you need to update or refresh data from these sources? | Transactional databases: near real-time updates; document repositories: daily batch updates; social media feeds: hourly updates; IoT sensor data: continuous real-time streaming; public datasets: monthly or quarterly updates. |
| What data formats do your generative AI models require as input? | Structured data: CSV, JSON, and SQL database tables; text data: plain text, PDF, and HTML; image data: JPEG, PNG, and TIFF; audio data: WAV and MP3; video data: MP4 and AVI. |
| What are your key data quality concerns for generative AI workloads? | Completeness: ensuring that no critical fields are missing; accuracy: verifying data correctness and eliminating errors; consistency: maintaining uniform formats and values across sources; timeliness: ensuring that data is up-to-date for real-time inference; relevance: confirming that data aligns with the specific generative AI task. |
| What are the key performance requirements (for example, response time, throughput, accuracy)? | 95% accuracy; < 500 ms response time; ability to handle 1000 requests/sec. High accuracy (95%\+), moderate accuracy (80-90%), best effort, and so on. |
| Do you have any other KPIs to measure the success of this use case ? | Key KPIs include error rate reduction, time savings per transaction, and customer satisfaction scores. |
| How much model accuracy is desired, and how does it balance with the cost? | High accuracy (>90%) with moderate cost, moderate accuracy (70-80%) with low cost, and so on. |
| What are the primary use cases or scenarios for the generative AI solution? | Customer service chatbot, content generation, product recommendation, and so on. |
| What are the target users or personas for the generative AI system? | Customer service agents, marketing team,employees, end users, and so on. |
| What is the expected volume of requests or users? | 1,000 requests per day; 10,000 monthly active users. |
| Are there any specific use case constraints or requirements? | Real-time response, multi-lingual support, data privacy, and so on. |
| Do you have an allocated budget for developing and maintaining the generative AI solution? | The initial development cost is estimated at $200,000, with annual maintenance costs of $50,000. |
| What is the projected return on investment (ROI) and payback period for this use case? | Expected ROI of 150% over three years, with a payback period of 18 months. |
| Are there any hidden costs or potential savings that should be considered? | Potential savings include reduced overtime costs. Hidden costs might involve additional training for staff. |
| What are the scalability and future expansion possibilities of this generative AI solution? | The solution is designed to scale with our operations, with the possibility of expanding to other departments in the future. |
| How do you ensure fairness and mitigate bias in your generative AI models? | We plan to mitigate bias through diverse data collection, regular bias audits, and implementation of bias mitigation techniques. |
| What processes do you have in place for addressing ethical concerns or unintended consequences? | We will manage ethical concerns through an established AI incident response plan, regular ethical risk assessments, an anonymous reporting system for employees, collaboration with external ethics experts, and continuous monitoring and adjustment of deployed models based on feedback. |
| How do you approach prioritizing and sequencing generative AI workload assessments across different projects and departments in your organization? | By conducting a high-level survey across all departments to identify potential generative AI use cases and evaluating them based on three key criteria: business impact, technical feasibility, and ethical considerations. Projects with high potential impact, lower technical barriers, and minimal ethical concerns are given priority. |
