# INFO 490: Cloud Computing with Google Cloud Platform
## University of Washington — Information School
### Autumn Quarter 2026

---

## COURSE OVERVIEW

**Course Title:** Cloud Computing with Google Cloud Platform
**Course Number:** INFO 490 / CSE 490G (cross-listed)
**Credits:** 5
**Prerequisites:** INFO 340 (Client-Side Development) or CSE 154 (Web Programming), or instructor permission
**Meeting Times:** Tuesdays and Thursdays, 10:30 AM – 12:20 PM
**Location:** Mary Gates Hall, Room 258
**Format:** In-person lectures with hands-on lab components
**Canvas Site:** canvas.uw.edu/courses/info490-gcp-aut2026

This course provides a comprehensive, hands-on introduction to cloud computing using Google Cloud Platform (GCP). Students will learn to design, deploy, and manage cloud-based applications and infrastructure using core GCP services. The course covers compute, storage, networking, data analytics, machine learning, serverless architectures, and cloud security. By the end of the quarter, students will be able to architect and deploy real-world cloud solutions and will be prepared to pursue the Google Cloud Associate Cloud Engineer certification.

---

## INSTRUCTOR AND TEACHING TEAM

### Instructor
**Dr. Sarah Chen**
- **Title:** Associate Professor, Information School
- **Email:** schen.cloud@uw.edu
- **Office:** Mary Gates Hall, Room 370E
- **Office Hours:** Tuesdays 1:00–2:30 PM, Thursdays 2:00–3:00 PM, or by appointment
- **Research Interests:** Cloud-native architectures, distributed systems, data engineering
- **Background:** Previously a Solutions Architect at Google Cloud; holds the Professional Cloud Architect and Professional Data Engineer certifications

### Teaching Assistants

**Marcus Rivera** (Lead TA)
- **Email:** mrivera.ta@uw.edu
- **Office Hours:** Mondays 3:00–5:00 PM, CSE2 Room 153
- **Lab Sections:** Lab A (Fridays 10:30–11:20 AM) and Lab B (Fridays 11:30 AM–12:20 PM)
- **Background:** Second-year MS student in Computer Science, focus on cloud infrastructure

**Priya Patel**
- **Email:** ppatel.ta@uw.edu
- **Office Hours:** Wednesdays 1:00–3:00 PM, Mary Gates Hall Commons
- **Lab Sections:** Lab C (Fridays 1:30–2:20 PM) and Lab D (Fridays 2:30–3:20 PM)
- **Background:** Second-year MS student in Information Management, focus on data analytics and ML

### Grader
**James Kim**
- **Email:** jkim.grader@uw.edu
- **Responsibilities:** Grading homework assignments and providing written feedback

---

## LEARNING OBJECTIVES

By the end of this course, students will be able to:

1. Explain core cloud computing concepts including IaaS, PaaS, SaaS, and serverless models
2. Navigate and use the Google Cloud Console, Cloud Shell, and the gcloud CLI effectively
3. Create and manage virtual machines using Compute Engine, including custom machine types, startup scripts, and instance groups
4. Design and implement cloud storage solutions using Cloud Storage, including bucket configuration, lifecycle policies, access control, and signed URLs
5. Configure Identity and Access Management (IAM) policies, service accounts, and organization-level security controls
6. Build and query data warehouses using BigQuery, including writing complex SQL, creating views, and managing datasets
7. Deploy and manage containerized applications on Google Kubernetes Engine (GKE), including creating clusters, writing Kubernetes manifests, and performing rolling updates
8. Build event-driven architectures using Cloud Functions and Pub/Sub
9. Use Vertex AI for machine learning workflows including training, deploying, and monitoring models
10. Deploy serverless applications with Cloud Run, set up CI/CD pipelines with Cloud Build, and manage container images with Artifact Registry
11. Apply cloud architecture best practices for cost optimization, high availability, and disaster recovery
12. Work collaboratively on a cloud-based project using version control and Infrastructure as Code principles

---

## REQUIRED MATERIALS AND TOOLS

### Required Textbook
- **"Google Cloud Certified Associate Cloud Engineer Study Guide"** by Dan Sullivan (Sybex/Wiley, 2nd Edition, 2024). ISBN: 978-1119871057. Available at the UW Bookstore and online retailers.

### Supplementary Resources (Free)
- Google Cloud Skills Boost (cloud.google.com/training) — Free labs and learning paths provided through the course
- Official Google Cloud Documentation (cloud.google.com/docs)
- Google Cloud Architecture Center (cloud.google.com/architecture)
- Coursera: "Google Cloud Fundamentals: Core Infrastructure" (audit for free)

### Required Tools and Accounts
- **Google Cloud Platform account:** Each student will receive $300 in GCP credits via a course coupon code distributed in Week 1. You must use your @uw.edu email to redeem.
- **Google Cloud SDK / gcloud CLI:** Install locally from cloud.google.com/sdk. We use version 480.0.0 or later.
- **GitHub account:** All lab submissions and the final project use GitHub repositories.
- **Visual Studio Code** (recommended IDE) with the Cloud Code extension installed
- **Docker Desktop:** Required for Weeks 6-7 (containers and GKE). Install from docker.com.
- **Terraform** (optional, introduced in Week 9): For Infrastructure as Code exercises

### Lab Environment
All lab work uses real GCP projects. Each student gets their own GCP project within the course organization. Do NOT use personal GCP accounts for coursework — always use the provided course project to ensure credits are applied correctly.

---

## COURSE SCHEDULE AND TOPICS

### WEEK 1: Introduction to Cloud Computing and GCP Fundamentals
**Lecture 1 (Tuesday): Cloud Computing Foundations**
- What is cloud computing? History and evolution
- Cloud service models: IaaS, PaaS, SaaS, FaaS (serverless)
- Cloud deployment models: public, private, hybrid, multi-cloud
- Why Google Cloud? Comparison with AWS and Azure
- GCP's global infrastructure: regions, zones, edge locations
- The GCP free tier and billing

**Lecture 2 (Thursday): Getting Started with GCP**
- Tour of the Google Cloud Console
- Cloud Shell and the gcloud CLI
- Projects, folders, and organizations in GCP's resource hierarchy
- Enabling APIs and managing services
- Setting up billing accounts and budgets
- Introduction to Cloud IAM (basic concepts)
- Demo: Creating your first project and VM

**Readings:** Sullivan textbook, Chapters 1-2
**Lab 1 assigned:** GCP Console & Cloud Shell Exploration (due end of Week 2)

---

### WEEK 2: Compute Engine — Virtual Machines in the Cloud
**Lecture 3 (Tuesday): Compute Engine Deep Dive**
- Creating and managing VM instances
- Machine types: general-purpose (E2, N2), compute-optimized (C2), memory-optimized (M2)
- Custom machine types: specifying vCPUs and memory
- Boot disks: public images, custom images, persistent disks (standard, SSD, balanced)
- Preemptible and Spot VMs for cost savings
- Startup scripts and metadata
- SSH access and OS Login

**Lecture 4 (Thursday): Networking and VM Management**
- VPC networks: default, auto-mode, custom-mode
- Subnets, IP ranges, and firewall rules
- Internal and external IP addresses, static IPs
- Instance groups: managed (MIG) and unmanaged
- Autoscaling policies (CPU, load balancing, custom metrics)
- Load balancing overview: HTTP(S), TCP/SSL, internal
- Live migration and availability policies
- Snapshots and machine images for backup

**Readings:** Sullivan textbook, Chapters 3-4
**Homework 1 assigned:** Compute Engine Architecture Design (due Week 4)

---

### WEEK 3: Cloud Storage — Object Storage and Data Management
**Lecture 5 (Tuesday): Cloud Storage Fundamentals**
- Object storage concepts: buckets, objects, metadata
- Storage classes: Standard, Nearline, Coldline, Archive
- Choosing the right storage class based on access patterns
- Creating and configuring buckets: location types (region, dual-region, multi-region)
- Uploading, downloading, and managing objects
- gsutil command-line tool and JSON API
- Composite objects and parallel uploads for large files
- Transfer Service for large-scale data migration

**Lecture 6 (Thursday): Storage Security, Lifecycle, and Advanced Features**
- Access control: uniform vs. fine-grained
- IAM policies on buckets vs. ACLs
- Signed URLs and signed policy documents for temporary access
- Object lifecycle management: automatic deletion, class transitions
- Object versioning and retention policies
- Requester Pays buckets
- Cloud Storage FUSE for mounting buckets as file systems
- Integration with other GCP services (BigQuery, Dataflow, Cloud Functions triggers)

**Readings:** Sullivan textbook, Chapter 6
**Lab 2 assigned:** Cloud Storage Data Pipeline (due end of Week 4)

---

### WEEK 4: Identity and Access Management (IAM) and Security
**Lecture 7 (Tuesday): IAM Fundamentals**
- The IAM model: members, roles, policies
- Types of members: Google accounts, service accounts, groups, domains, allUsers, allAuthenticatedUsers
- Role types: basic (Owner, Editor, Viewer), predefined, custom
- The principle of least privilege
- IAM policy binding and conditions
- Resource hierarchy and policy inheritance (organization → folder → project → resource)
- IAM Recommender and Policy Analyzer

**Lecture 8 (Thursday): Service Accounts, Security, and Compliance**
- Service accounts: user-managed vs. Google-managed
- Service account keys (and why to avoid them)
- Workload Identity Federation for keyless authentication
- Organization policies and constraints
- VPC Service Controls and access context
- Cloud Audit Logs: Admin Activity, Data Access, System Event
- Secret Manager for storing API keys, passwords, certificates
- Cloud KMS for encryption key management
- Security Command Center overview
- Best practices for GCP security

**Readings:** Sullivan textbook, Chapter 5
**Homework 1 due (Thursday)**
**Homework 2 assigned:** IAM Policy Design (due Week 6)
**Lab 1 due (end of week)**

---

### WEEK 5: BigQuery — Data Warehousing and Analytics
**Lecture 9 (Tuesday): BigQuery Fundamentals**
- What is BigQuery? Serverless, petabyte-scale data warehouse
- BigQuery architecture: Dremel execution engine, Colossus storage, Jupiter network
- Datasets, tables, and views
- Loading data: batch loading, streaming inserts, external tables
- Supported formats: CSV, JSON, Avro, Parquet, ORC
- BigQuery Storage API for fast reads
- Partitioned tables: ingestion-time, column-based (DATE, TIMESTAMP, INTEGER RANGE)
- Clustered tables for query optimization

**Lecture 10 (Thursday): Advanced BigQuery and SQL Analytics**
- Standard SQL in BigQuery: window functions, CTEs, subqueries, UDFs
- Materialized views and authorized views
- BigQuery ML: training models directly in SQL (CREATE MODEL)
- BigQuery BI Engine for fast dashboards
- Cost management: on-demand vs. flat-rate pricing, slot reservations
- Query optimization: avoiding SELECT *, using partitioning and clustering, query execution plan analysis
- Scheduling queries and data transfer service
- Connecting BigQuery to Looker Studio for visualization
- BigQuery Omni for multi-cloud analytics

**Readings:** Sullivan textbook, Chapter 9 (Data Analytics sections)
**Lab 3 assigned:** BigQuery Data Analysis Project (due end of Week 6)

---

### WEEK 6: Google Kubernetes Engine (GKE) — Container Orchestration
**Lecture 11 (Tuesday): Containers and Kubernetes Fundamentals**
- What are containers? Containers vs. VMs
- Docker basics: images, containers, Dockerfiles, layers
- Building and pushing images to Artifact Registry
- Kubernetes concepts: pods, nodes, clusters
- The Kubernetes control plane: API server, scheduler, controller manager, etcd
- kubectl CLI basics
- GKE cluster modes: Autopilot vs. Standard
- Creating a GKE cluster: node pools, machine types, networking

**Lecture 12 (Thursday): Deploying Applications on GKE**
- Kubernetes workloads: Deployments, ReplicaSets, StatefulSets, DaemonSets, Jobs
- Writing YAML manifests for deployments
- Services: ClusterIP, NodePort, LoadBalancer
- Ingress controllers and managed certificates
- ConfigMaps and Secrets
- Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA)
- Rolling updates and rollbacks
- Health checks: liveness, readiness, and startup probes
- Monitoring with Cloud Monitoring and Cloud Logging
- GKE cost optimization: Spot pods, right-sizing

**Readings:** Sullivan textbook, Chapter 7
**Homework 2 due (Thursday)**
**Lab 4 assigned:** Deploy a Microservices App on GKE (due end of Week 7)
**Lab 2 due (end of week)**

---

### WEEK 7: Serverless — Cloud Functions and Pub/Sub
**Lecture 13 (Tuesday): Cloud Functions**
- Serverless computing concepts: no infrastructure management, auto-scaling, pay-per-invocation
- Cloud Functions (2nd gen) overview: built on Cloud Run
- Supported runtimes: Python, Node.js, Go, Java, .NET, Ruby, PHP
- HTTP-triggered functions vs. event-driven functions
- Writing and deploying Cloud Functions
- Environment variables and Secret Manager integration
- Cloud Functions concurrency and min/max instances
- Testing locally with the Functions Framework
- Connecting Cloud Functions to other GCP services

**Lecture 14 (Thursday): Pub/Sub and Event-Driven Architecture**
- Pub/Sub overview: topics, subscriptions, messages, acknowledgments
- Push vs. pull subscriptions
- Message ordering and exactly-once delivery
- Dead-letter topics for failed messages
- Pub/Sub Lite for high-throughput, lower-cost scenarios
- Event-driven architecture patterns: fan-out, fan-in, choreography
- Eventarc: unified eventing for GCP
- Building a data pipeline: Cloud Storage → Pub/Sub → Cloud Functions → BigQuery
- Monitoring Pub/Sub with Cloud Monitoring

**Readings:** Sullivan textbook, Chapter 8
**Homework 3 assigned:** Event-Driven Pipeline Design (due Week 9)
**Lab 3 due (end of week)**

---

### WEEK 8: Vertex AI — Machine Learning on GCP (MIDTERM WEEK)
**Lecture 15 (Tuesday): MIDTERM EXAM**
- Covers Weeks 1-7 (Cloud fundamentals, Compute Engine, Cloud Storage, IAM, BigQuery, GKE, Cloud Functions, Pub/Sub)
- Format: 50 multiple-choice questions, 3 short-answer questions, 1 architecture design question
- Duration: 110 minutes
- Open-note (one 8.5"×11" handwritten or typed reference sheet, both sides)
- No internet access during exam

**Lecture 16 (Thursday): Introduction to Vertex AI**
- Machine learning on GCP: history and evolution
- Vertex AI platform overview: unified ML platform
- AutoML: training models without code (image, text, tabular, video)
- Custom training: using pre-built containers and custom containers
- Vertex AI Workbench (managed Jupyter notebooks)
- Feature Store for managing ML features
- Model Registry and model versioning
- Deploying models to endpoints for online prediction
- Batch prediction for large datasets
- Model monitoring and drift detection

**Readings:** Sullivan textbook, Chapter 10
**Lab 5 assigned:** Vertex AI AutoML Classification (due end of Week 9)
**Lab 4 due (end of week)**

---

### WEEK 9: Cloud Run, CI/CD, and Infrastructure as Code
**Lecture 17 (Tuesday): Cloud Run — Serverless Containers**
- Cloud Run overview: fully managed serverless for containers
- Cloud Run vs. Cloud Functions vs. GKE: when to use which
- Deploying a container to Cloud Run
- Custom domains and Cloud Run URL mapping
- Concurrency settings and autoscaling (0 to N)
- Cloud Run Jobs for batch workloads
- Cloud Run with Cloud SQL (connecting to databases)
- Traffic splitting for canary deployments
- Cloud Run integrations: Pub/Sub push, Cloud Scheduler

**Lecture 18 (Thursday): CI/CD and Infrastructure as Code**
- Continuous Integration / Continuous Deployment concepts
- Cloud Build: build steps, substitutions, triggers
- Cloud Build with GitHub: automatic builds on push
- Artifact Registry: storing Docker images, language packages
- Cloud Deploy for managed continuous delivery
- Infrastructure as Code (IaC) concepts
- Terraform with GCP: providers, resources, modules
- Terraform state management with Cloud Storage backend
- Google Cloud Deployment Manager (brief overview)
- GitOps patterns with Config Sync

**Readings:** Sullivan textbook, Chapter 11
**Homework 3 due (Thursday)**
**Homework 4 assigned:** CI/CD Pipeline Implementation (due Week 10 Tuesday)
**Lab 5 due (end of week)**

---

### WEEK 10: Cloud Architecture, Cost Optimization, and Final Project Presentations
**Lecture 19 (Tuesday): Cloud Architecture Best Practices**
- Google Cloud Architecture Framework: operational excellence, security, reliability, performance, cost optimization
- High availability and disaster recovery patterns
- Multi-region architectures
- Designing for failure: circuit breakers, retries, exponential backoff
- Microservices vs. monoliths on GCP
- API Gateway and Cloud Endpoints
- Cloud CDN and Cloud Armor for web applications
- Cloud Interconnect and Cloud VPN for hybrid connectivity
- Migration strategies: lift-and-shift, move-and-improve, rebuild
- Cost optimization: committed use discounts, sustained use discounts, right-sizing recommendations
- Billing reports, budgets, and alerts
- Carbon footprint and sustainable cloud computing

**Lecture 20 (Thursday): Final Project Presentations and Course Wrap-Up**
- Student teams present final projects (15 minutes per team)
- Peer evaluation and Q&A
- Course review and key takeaways
- Guidance on Google Cloud certification paths
- Career opportunities in cloud computing

**Homework 4 due (Tuesday)**
**Final Project due (Thursday before presentations)**
**Lab 6 due (end of week)**

---

## ASSIGNMENTS

### Homework Assignments (5 total)

#### Homework 1: Compute Engine Architecture Design
- **Assigned:** Week 2 (Thursday)
- **Due:** Week 4 (Thursday) by 11:59 PM Pacific
- **Points:** 50
- **Description:** Design a compute infrastructure for a hypothetical web application. You will create an architecture diagram showing VM configurations, networking setup (VPC, subnets, firewall rules), load balancing, autoscaling, and high availability across zones. Write a 2-page justification explaining your machine type choices, cost estimates, and trade-offs.
- **Deliverables:** Architecture diagram (draw.io or Lucidchart), written justification (PDF), cost estimate spreadsheet
- **Submission:** Upload to Canvas

#### Homework 2: IAM Policy Design
- **Assigned:** Week 4 (Thursday)
- **Due:** Week 6 (Thursday) by 11:59 PM Pacific
- **Points:** 50
- **Description:** Given a scenario of a mid-size company with multiple teams (development, QA, operations, data science, management), design a comprehensive IAM strategy. Define custom roles, service accounts, resource hierarchy (org → folders → projects), and organization policies. Identify potential security risks and how your design mitigates them.
- **Deliverables:** IAM policy document (PDF) with role definitions, resource hierarchy diagram, security analysis
- **Submission:** Upload to Canvas

#### Homework 3: Event-Driven Pipeline Design
- **Assigned:** Week 7 (Thursday)
- **Due:** Week 9 (Thursday) by 11:59 PM Pacific
- **Points:** 50
- **Description:** Design an event-driven data processing pipeline using Pub/Sub, Cloud Functions, Cloud Storage, and BigQuery. The scenario involves processing incoming sensor data from IoT devices: data arrives in Cloud Storage, triggers processing via Pub/Sub and Cloud Functions, transforms and loads into BigQuery for analysis. Include error handling, dead-letter topics, and monitoring.
- **Deliverables:** Architecture diagram, Cloud Functions code (Python), Pub/Sub topic/subscription configuration, monitoring dashboard screenshot
- **Submission:** GitHub repository link + Canvas upload

#### Homework 4: CI/CD Pipeline Implementation
- **Assigned:** Week 9 (Thursday)
- **Due:** Week 10 (Tuesday) by 11:59 PM Pacific
- **Points:** 50
- **Description:** Implement a CI/CD pipeline for a sample web application using Cloud Build, Artifact Registry, and Cloud Run. The pipeline should automatically build a Docker image on git push, run tests, push to Artifact Registry, and deploy to Cloud Run with traffic splitting (90/10 canary). Include a Terraform configuration for the Cloud Run service.
- **Deliverables:** GitHub repository with application code, Dockerfile, cloudbuild.yaml, Terraform files, and a README documenting the pipeline
- **Submission:** GitHub repository link + Canvas upload

#### Homework 5: Cloud Architecture Case Study
- **Assigned:** Week 10 (Tuesday) — posted on Canvas
- **Due:** Finals Week Tuesday by 11:59 PM Pacific
- **Points:** 50
- **Description:** Given a detailed business scenario (an e-commerce company migrating from on-premises to GCP), create a comprehensive cloud architecture proposal. Address compute, storage, databases, networking, security, CI/CD, monitoring, cost optimization, and disaster recovery. Present trade-offs between different GCP services and justify your choices.
- **Deliverables:** Architecture proposal document (5-7 pages), architecture diagrams, cost projection, migration timeline
- **Submission:** Upload to Canvas

---

### Labs (8 total)

#### Lab 1: GCP Console & Cloud Shell Exploration
- **Assigned:** Week 1
- **Due:** End of Week 4
- **Points:** 25
- **Description:** Complete a guided exploration of the GCP Console and Cloud Shell. Tasks include: navigating the console, using the gcloud CLI to create and manage resources, setting up a project, enabling APIs, creating a budget alert, and writing a shell script that automates the creation of 3 VMs with different machine types in different zones.
- **Key Commands:** `gcloud projects create`, `gcloud services enable`, `gcloud compute instances create`, `gcloud config set`
- **Deliverables:** Screenshot portfolio, shell script, answers to 10 exploration questions

#### Lab 2: Cloud Storage Data Pipeline
- **Assigned:** Week 3
- **Due:** End of Week 6
- **Points:** 25
- **Description:** Build a data pipeline using Cloud Storage. Tasks: create buckets with different storage classes, configure lifecycle rules (transition Standard → Nearline after 30 days, delete after 365 days), enable versioning, create a signed URL for temporary access, upload a dataset and write a Python script that uses the Cloud Storage client library to process files in a bucket and generate a summary report.
- **Key Skills:** gsutil, Cloud Storage Python client library, lifecycle policies, signed URLs
- **Deliverables:** Python script, lifecycle policy JSON, screenshots of bucket configurations, summary report output

#### Lab 3: BigQuery Data Analysis Project
- **Assigned:** Week 5
- **Due:** End of Week 7
- **Points:** 30
- **Description:** Load a public dataset into BigQuery (the Chicago taxi trips dataset or similar), create partitioned and clustered tables, write 8 analytical queries using window functions, CTEs, and subqueries. Create a BigQuery ML model to predict trip duration. Build a Looker Studio dashboard with at least 4 visualizations. Analyze query costs and optimize with partitioning.
- **Key Skills:** BigQuery SQL, partitioning, clustering, BigQuery ML, Looker Studio
- **Deliverables:** SQL queries file, BigQuery ML model evaluation results, Looker Studio dashboard (shared link), cost analysis document

#### Lab 4: Deploy a Microservices App on GKE
- **Assigned:** Week 6
- **Due:** End of Week 8
- **Points:** 30
- **Description:** Deploy a multi-service application on GKE. The application has a frontend (React), a backend API (Python/Flask), and a Redis cache. Tasks: create a GKE Autopilot cluster, write Dockerfiles for each service, push images to Artifact Registry, write Kubernetes YAML manifests (Deployments, Services, ConfigMaps), set up an Ingress with a managed SSL certificate, configure HPA, perform a rolling update, and test rollback.
- **Key Skills:** Docker, Kubernetes YAML, kubectl, GKE Autopilot, Ingress, HPA
- **Deliverables:** GitHub repository with all Dockerfiles, Kubernetes manifests, screenshots showing running pods and services, brief write-up of the deployment process

#### Lab 5: Vertex AI AutoML Classification
- **Assigned:** Week 8
- **Due:** End of Week 9
- **Points:** 25
- **Description:** Use Vertex AI AutoML to train an image classification model. Tasks: prepare and upload a labeled image dataset to Cloud Storage, create a Vertex AI dataset, train an AutoML model, evaluate model performance (precision, recall, confusion matrix), deploy the model to an endpoint, and make predictions using the Vertex AI Python SDK. Compare the AutoML model's performance with a simple custom model trained in a Vertex AI Workbench notebook.
- **Key Skills:** Vertex AI Console, AutoML, model deployment, Vertex AI SDK
- **Deliverables:** Jupyter notebook with custom model, AutoML evaluation screenshots, prediction results, comparison analysis document

#### Lab 6: Serverless Event Pipeline
- **Assigned:** Week 9 (during lab section)
- **Due:** End of Week 10
- **Points:** 25
- **Description:** Build an end-to-end serverless pipeline: a Cloud Function is triggered when a file is uploaded to a Cloud Storage bucket, it publishes a message to Pub/Sub, another Cloud Function consumes the message and processes the data, then writes results to BigQuery. Add a Cloud Scheduler job that triggers a Cloud Run service to generate a daily summary report. Implement error handling with a dead-letter topic.
- **Key Skills:** Cloud Functions, Pub/Sub, Cloud Storage triggers, Cloud Scheduler, Cloud Run, BigQuery
- **Deliverables:** GitHub repository with all function code, deployment scripts, architecture diagram, screenshots of working pipeline

#### Lab 7: Terraform Infrastructure as Code (Bonus Lab)
- **Assigned:** Week 9
- **Due:** Finals Week Friday
- **Points:** 15 (bonus)
- **Description:** Recreate the infrastructure from Labs 4 and 6 using Terraform. Write Terraform configurations for: a GKE cluster, Cloud Storage buckets, Pub/Sub topics and subscriptions, Cloud Functions, BigQuery datasets and tables, IAM bindings, and Cloud Run services. Use Terraform modules for reusable components and manage state in a Cloud Storage backend.
- **Key Skills:** Terraform HCL, GCP Terraform provider, modules, state management
- **Deliverables:** GitHub repository with Terraform files, terraform plan output, README with setup instructions

#### Lab 8: Cloud Security Audit (Bonus Lab)
- **Assigned:** Week 10
- **Due:** Finals Week Friday
- **Points:** 15 (bonus)
- **Description:** Perform a security audit of your course GCP project. Use Security Command Center to identify vulnerabilities, review IAM policies for over-privileged accounts, check for publicly accessible resources, review audit logs for suspicious activity, and set up a Cloud Monitoring alerting policy for unauthorized access attempts. Write a security report with findings and remediation recommendations.
- **Key Skills:** Security Command Center, IAM Policy Analyzer, Cloud Audit Logs, Cloud Monitoring
- **Deliverables:** Security audit report (3-5 pages), screenshots of findings and remediations

---

### Final Project

#### Team-Based Cloud Architecture Project
- **Team Size:** 3-4 students (assigned in Week 3)
- **Proposal Due:** Week 5 (Thursday) by 11:59 PM Pacific
- **Check-in Presentation:** Week 8 (lab section) — 5 minutes per team
- **Final Submission:** Week 10 (Thursday) by 9:00 AM Pacific (before class)
- **Presentation:** Week 10 (Thursday) during class — 15 minutes per team + 5 minutes Q&A
- **Points:** 150

**Description:** Design and implement a cloud-native application on GCP that solves a real-world problem. The application must use at least 5 different GCP services and demonstrate cloud architecture best practices. Teams will deliver a working application, architecture documentation, a cost analysis, and a live demo.

**Requirements:**
- Use at least 5 GCP services (e.g., Compute Engine or Cloud Run for compute, Cloud Storage for static assets, BigQuery for analytics, Pub/Sub for messaging, Vertex AI for ML features)
- Implement CI/CD using Cloud Build
- Include monitoring and logging with Cloud Monitoring and Cloud Logging
- Write Infrastructure as Code (Terraform or Deployment Manager) for at least 3 services
- Include a security analysis with IAM roles and service accounts documented
- Provide a cost estimate for running the application at production scale

**Deliverables:**
- GitHub repository with all code, configurations, and documentation
- Architecture document (5-8 pages) with diagrams
- 15-minute presentation with live demo
- Peer evaluation form (each team member evaluates their teammates)

**Past Project Examples:**
- Real-time air quality monitoring dashboard using IoT data, Pub/Sub, BigQuery, and Looker Studio
- Image-based plant disease detection app using Vertex AI AutoML and Cloud Run
- Event ticketing platform with GKE microservices, Cloud SQL, and Redis
- Automated document processing pipeline using Document AI, Cloud Functions, and BigQuery
- Campus shuttle tracking app with Maps API, Firestore, and Cloud Run

---

## GRADING

### Grade Components
| Component | Points | Percentage |
|---|---|---|
| Homework Assignments (5 × 50) | 250 | 31.25% |
| Labs (6 required × avg 27 pts) | 160 | 20.00% |
| Midterm Exam | 100 | 12.50% |
| Final Project | 150 | 18.75% |
| Participation & Discussion | 50 | 6.25% |
| Final Exam | 90 | 11.25% |
| **Total** | **800** | **100%** |
| Bonus Labs (2 × 15) | +30 | +3.75% |

### Grading Scale
| Grade | Percentage | GPA |
|---|---|---|
| A | 93–100% | 4.0 |
| A- | 90–92% | 3.7 |
| B+ | 87–89% | 3.3 |
| B | 83–86% | 3.0 |
| B- | 80–82% | 2.7 |
| C+ | 77–79% | 2.3 |
| C | 73–76% | 2.0 |
| C- | 70–72% | 1.7 |
| D+ | 67–69% | 1.3 |
| D | 60–66% | 1.0 |
| F | Below 60% | 0.0 |

### Late Policy
- Assignments submitted up to 24 hours late receive a 10% penalty
- Assignments submitted 24-48 hours late receive a 25% penalty
- Assignments submitted more than 48 hours late receive no credit
- Each student gets TWO free late day tokens (each extends a deadline by 24 hours, no penalty). Email the TA before the deadline to use a token.
- Lab deadlines have a built-in 1-week buffer (assigned 2-3 weeks before due). No additional extensions for labs except in documented emergencies.
- The final project deadline is firm — no late submissions accepted.

---

## EXAMS

### Midterm Exam
- **Date:** Week 8, Tuesday, during class (10:30 AM – 12:20 PM)
- **Coverage:** Weeks 1-7 (Cloud fundamentals, Compute Engine, Cloud Storage, IAM, BigQuery, GKE, Cloud Functions, Pub/Sub)
- **Format:**
  - 30 multiple-choice questions (2 points each = 60 points), 3 short-answer questions (8 points each = 24 points), 1 architecture design question (16 points)
  - Total: 100 points
- **Duration:** 110 minutes
- **Reference Sheet:** One 8.5"×11" handwritten or typed reference sheet (both sides allowed)
- **No internet access, no electronic devices except the reference sheet**

**Study Guide Topics:**
- Cloud service models and deployment models
- GCP resource hierarchy
- Compute Engine machine types, instance groups, autoscaling
- VPC networking, firewall rules, load balancing
- Cloud Storage classes, lifecycle policies, access control
- IAM roles (basic, predefined, custom), service accounts
- BigQuery architecture, SQL syntax, partitioning, clustering
- Kubernetes concepts, GKE cluster modes, deployments, services
- Cloud Functions triggers, Pub/Sub topics/subscriptions

### Final Exam
- **Date:** Finals week, scheduled by UW Registrar (check UW finals schedule)
- **Coverage:** Weeks 1-10 (comprehensive, with emphasis on Weeks 8-10 material)
- **Format:**
  - 25 multiple-choice questions (2 points each = 50 points), 2 short-answer questions (10 points each = 20 points), 1 comprehensive architecture design question (20 points)
  - Total: 90 points
- **Duration:** 120 minutes
- **Reference Sheet:** One 8.5"×11" handwritten or typed reference sheet (both sides allowed)

**Additional Study Topics for Final (beyond midterm material):**
- Vertex AI: AutoML, custom training, model deployment, Feature Store
- Cloud Run: deployment, scaling, traffic splitting, Jobs
- CI/CD: Cloud Build, Artifact Registry, Cloud Deploy
- Terraform basics: resources, providers, modules, state
- Cloud architecture best practices: HA, DR, cost optimization
- Migration strategies: lift-and-shift, move-and-improve, rebuild
- Security: VPC Service Controls, Security Command Center, Cloud KMS

---

## COURSE POLICIES

### Attendance and Participation
- Attendance is expected but not strictly required for lectures
- Lab section attendance is required (each lab section includes a brief quiz worth participation points)
- Active participation in class discussions, Piazza/Ed Discussion, and peer code reviews contributes to the participation grade
- Missing more than 3 lab sections without documented reason will result in loss of participation points

### Academic Integrity
- All individual assignments must be your own work
- You may discuss concepts and approaches with classmates but must write your own code and documents
- Using AI tools (ChatGPT, GitHub Copilot, etc.) is permitted for learning and debugging but you must:
  1. Cite any AI-generated code in your submissions
  2. Be able to explain every line of code you submit
  3. Not use AI tools during exams
- Plagiarism or unauthorized collaboration will result in a zero on the assignment and potential referral to the UW Community Standards & Student Conduct office
- For the final project, all team members must contribute equitably (peer evaluations are used to adjust individual grades)

### Communication
- **Piazza/Ed Discussion:** Primary platform for questions. Post questions publicly when possible so all students benefit. TAs aim to respond within 12 hours on weekdays.
- **Email:** Use for private matters only (grade disputes, personal issues, accommodations). Include "INFO 490" in the subject line. Expect a response within 24-48 hours.
- **Office Hours:** Come with specific questions or problems. No appointment needed during posted hours.
- **Canvas Announcements:** Check regularly for important updates, deadline reminders, and resource links.

### Accessibility
- The University of Washington is committed to providing access and reasonable accommodation in its services, programs, activities, education, and employment for individuals with disabilities.
- Students with documented disabilities should contact Disability Resources for Students (DRS) at drs.washington.edu to establish accommodations.
- Please share your DRS accommodation letter with Dr. Chen within the first two weeks of the quarter.

### Religious Accommodations
- Washington state law requires that UW develop a policy for accommodation of student absences to allow students to take holidays for reasons of faith or conscience.
- Students must request accommodations within the first two weeks of the quarter.

---

## DETAILED LECTURE NOTES AND KEY CONCEPTS

### Cloud Computing Fundamentals

**Shared Responsibility Model:**
- In IaaS (e.g., Compute Engine): Google manages physical infrastructure, hypervisor; you manage OS, middleware, applications, data
- In PaaS (e.g., App Engine): Google also manages OS and middleware; you manage applications and data
- In SaaS (e.g., Google Workspace): Google manages everything; you manage data and access

**GCP Global Infrastructure:**
- 40+ regions worldwide (as of 2026)
- Each region has 2-4 zones (independent failure domains)
- 187+ edge locations for Cloud CDN
- Private fiber network connecting all data centers (Jupiter network for internal, B4 for external)
- Key regions for this class: us-west1 (Oregon), us-central1 (Iowa), us-east1 (South Carolina)

**GCP Resource Hierarchy:**
```
Organization (uw.edu)
├── Folder (Information School)
│   ├── Folder (Courses)
│   │   ├── Project (info490-student-jdoe)
│   │   ├── Project (info490-student-msmith)
│   │   └── Project (info490-shared-resources)
│   └── Folder (Research)
│       └── Project (ischool-research-lab)
└── Folder (Computer Science)
    └── Project (cse490g-shared)
```

### Compute Engine Key Concepts

**Machine Type Families:**
- **E2:** Cost-optimized, shared-core available (e2-micro, e2-small, e2-medium). Best for: dev/test, small apps
- **N2/N2D:** Balanced price/performance. Best for: web servers, app servers, databases
- **C2/C2D:** Compute-optimized, highest per-core performance. Best for: gaming servers, HPC, batch processing
- **M2/M3:** Memory-optimized (up to 12 TB RAM). Best for: SAP HANA, in-memory databases
- **A2/A3:** Accelerator-optimized (NVIDIA GPUs). Best for: ML training, inference, rendering
- **T2D/T2A:** Arm-based (Tau), cost-effective for scale-out workloads

**Persistent Disk Types:**
- **pd-standard:** HDD, cheapest, good for bulk storage. IOPS: 0.75 read, 1.5 write per GB
- **pd-balanced:** SSD, good balance of cost and performance. IOPS: 6 read, 6 write per GB
- **pd-ssd:** SSD, highest performance. IOPS: 30 read, 30 write per GB
- **pd-extreme:** Highest IOPS/throughput for demanding workloads

**Key gcloud commands for Compute Engine:**
```bash
# Create a VM
gcloud compute instances create my-vm \
    --zone=us-west1-a \
    --machine-type=e2-medium \
    --image-family=debian-12 \
    --image-project=debian-cloud \
    --boot-disk-size=50GB \
    --boot-disk-type=pd-balanced \
    --tags=http-server

# Create a firewall rule
gcloud compute firewall-rules create allow-http \
    --network=default \
    --allow=tcp:80 \
    --target-tags=http-server

# Create an instance template
gcloud compute instance-templates create web-template \
    --machine-type=e2-medium \
    --image-family=debian-12 \
    --image-project=debian-cloud \
    --metadata-from-file=startup-script=startup.sh

# Create a managed instance group
gcloud compute instance-groups managed create web-mig \
    --template=web-template \
    --size=3 \
    --zone=us-west1-a
```

### Cloud Storage Key Concepts

**Storage Classes and Use Cases:**
- **Standard:** Frequently accessed data, no minimum storage duration. $0.020/GB/month (us-central1)
- **Nearline:** Data accessed less than once a month. $0.010/GB/month. 30-day minimum storage.
- **Coldline:** Data accessed less than once a quarter. $0.004/GB/month. 90-day minimum storage.
- **Archive:** Data accessed less than once a year (backups, compliance). $0.0012/GB/month. 365-day minimum.

**Lifecycle Rule Example (JSON):**
```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30, "matchesStorageClass": ["STANDARD"]}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
```

**Key gsutil commands:**
```bash
# Create a bucket
gsutil mb -l us-west1 gs://my-info490-bucket/

# Upload files
gsutil cp local-file.csv gs://my-info490-bucket/data/

# Set lifecycle policy
gsutil lifecycle set lifecycle.json gs://my-info490-bucket/

# Generate a signed URL (valid for 1 hour)
gsutil signurl -d 1h service-account-key.json gs://my-info490-bucket/data/report.csv

# Enable versioning
gsutil versioning set on gs://my-info490-bucket/
```

### IAM Key Concepts

**Role Types:**
- **Basic roles (avoid in production):** Owner, Editor, Viewer — too broad
- **Predefined roles:** Granular, service-specific (e.g., `roles/storage.objectViewer`, `roles/bigquery.dataEditor`)
- **Custom roles:** User-defined with specific permissions for your organization's needs

**Common Predefined Roles Students Should Know:**
- `roles/compute.instanceAdmin.v1` — Full control of Compute Engine instances
- `roles/storage.objectAdmin` — Full control of Cloud Storage objects
- `roles/storage.objectViewer` — Read-only access to objects
- `roles/bigquery.dataEditor` — Create/update/delete BigQuery data
- `roles/bigquery.jobUser` — Run BigQuery jobs
- `roles/container.developer` — Access to Kubernetes API in GKE
- `roles/cloudfunctions.developer` — Deploy and manage Cloud Functions
- `roles/run.developer` — Deploy and manage Cloud Run services
- `roles/iam.serviceAccountUser` — Act as a service account
- `roles/viewer` — Read access to all resources (basic role, use sparingly)

**Service Account Best Practices:**
1. Create dedicated service accounts for each application/service
2. Grant minimum necessary permissions (least privilege)
3. Avoid downloading service account keys — use Workload Identity Federation or attached service accounts
4. Rotate keys regularly if you must use them
5. Monitor service account usage with audit logs

### BigQuery Key Concepts

**BigQuery Pricing:**
- **On-demand:** $6.25 per TB of data processed by queries
- **Capacity (editions):** Standard ($0.04/slot/hour), Enterprise ($0.06/slot/hour), Enterprise Plus ($0.10/slot/hour)
- **Storage:** $0.02/GB/month for active, $0.01/GB/month for long-term (after 90 days, automatic)
- **Streaming inserts:** $0.01 per 200 MB
- **Free tier:** 1 TB query processing and 10 GB storage per month

**Useful BigQuery SQL Patterns:**
```sql
-- Window function: Running total of daily sales
SELECT
  date,
  sales,
  SUM(sales) OVER (ORDER BY date) AS running_total
FROM `project.dataset.daily_sales`;

-- CTE: Find above-average performers
WITH avg_scores AS (
  SELECT AVG(score) as mean_score FROM `project.dataset.students`
)
SELECT s.name, s.score
FROM `project.dataset.students` s, avg_scores a
WHERE s.score > a.mean_score;

-- Partitioned table creation
CREATE TABLE `project.dataset.events`
PARTITION BY DATE(event_timestamp)
CLUSTER BY user_id, event_type
AS SELECT * FROM `project.dataset.raw_events`;

-- BigQuery ML: Linear regression
CREATE OR REPLACE MODEL `project.dataset.trip_duration_model`
OPTIONS(model_type='linear_reg', input_label_cols=['trip_duration']) AS
SELECT
  pickup_latitude, pickup_longitude,
  dropoff_latitude, dropoff_longitude,
  trip_duration
FROM `project.dataset.taxi_trips`
WHERE trip_duration > 0 AND trip_duration < 7200;
```

### Kubernetes / GKE Key Concepts

**Kubernetes Architecture:**
- **Control Plane:** API Server (entry point for all requests), Scheduler (assigns pods to nodes), Controller Manager (maintains desired state), etcd (key-value store for cluster state)
- **Worker Nodes:** kubelet (node agent), kube-proxy (networking), container runtime (containerd)
- **GKE Autopilot vs. Standard:**
  - Autopilot: Google manages nodes, pay per pod, enforces best practices, simpler
  - Standard: You manage node pools, more control, can run privileged containers

**Sample Kubernetes Deployment YAML:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: us-west1-docker.pkg.dev/my-project/my-repo/web-app:v1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: "250m"
            memory: "512Mi"
          limits:
            cpu: "500m"
            memory: "1Gi"
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: web-app-service
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 8080
```

### Cloud Functions Key Concepts

**Cloud Functions (2nd Gen) vs. 1st Gen:**
- 2nd gen is built on Cloud Run (same infrastructure)
- 2nd gen supports concurrency (multiple requests per instance)
- 2nd gen has longer timeout (up to 60 min vs. 9 min)
- 2nd gen supports larger instances (up to 16 GB RAM, 4 vCPUs)
- 2nd gen uses Eventarc for event triggers (more event sources)

**Sample Cloud Function (Python, HTTP Trigger):**
```python
import functions_framework
from google.cloud import bigquery

@functions_framework.http
def process_request(request):
    """HTTP-triggered Cloud Function."""
    request_json = request.get_json(silent=True)
    
    if not request_json or 'query' not in request_json:
        return ('Missing query parameter', 400)
    
    client = bigquery.Client()
    query_job = client.query(request_json['query'])
    results = [dict(row) for row in query_job]
    
    return {'results': results, 'row_count': len(results)}
```

**Sample Cloud Function (Python, Cloud Storage Trigger):**
```python
import functions_framework
from google.cloud import storage, pubsub_v1

@functions_framework.cloud_event
def process_upload(cloud_event):
    """Triggered when a file is uploaded to Cloud Storage."""
    data = cloud_event.data
    bucket_name = data["bucket"]
    file_name = data["name"]
    
    print(f"Processing file: gs://{bucket_name}/{file_name}")
    
    # Publish to Pub/Sub for downstream processing
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('my-project', 'file-uploads')
    publisher.publish(topic_path, data=file_name.encode('utf-8'),
                     bucket=bucket_name)
```

### Pub/Sub Key Concepts

**Message Flow:**
1. Publisher sends message to a Topic
2. Topic fans out messages to all Subscriptions
3. Each Subscription delivers messages to Subscribers
4. Subscriber acknowledges message after processing

**Delivery Guarantees:**
- At-least-once delivery (default)
- Exactly-once delivery (available with pull subscriptions, ordering enabled)
- Message ordering with ordering keys
- Messages retained for 7 days by default (configurable: 10 min to 31 days)

### Vertex AI Key Concepts

**Vertex AI Services:**
- **AutoML:** No-code ML model training for image, text, tabular, video data
- **Custom Training:** Use pre-built containers (TensorFlow, PyTorch, scikit-learn, XGBoost) or custom containers
- **Vertex AI Workbench:** Managed Jupyter notebooks with pre-installed ML libraries
- **Feature Store:** Centralized repository for ML features with point-in-time lookups
- **Model Registry:** Version and manage trained models
- **Endpoints:** Deploy models for online (real-time) prediction
- **Batch Prediction:** Run predictions on large datasets asynchronously
- **Pipelines:** Orchestrate ML workflows with Kubeflow Pipelines or TFX
- **Model Monitoring:** Detect prediction drift and feature skew

### Cloud Run Key Concepts

**Cloud Run Features:**
- Fully managed serverless platform for containers
- Scale to zero (pay nothing when no traffic)
- Scale up to 1000+ instances automatically
- Deploy any container that listens on a port
- Supports custom domains, WebSockets, gRPC, HTTP/2
- Concurrency: up to 1000 requests per container instance
- Maximum timeout: 3600 seconds (1 hour) for HTTP, 24 hours for jobs

**Cloud Run vs. Cloud Functions vs. GKE:**
| Feature | Cloud Run | Cloud Functions | GKE |
|---|---|---|---|
| Unit of deployment | Container | Function | Pod/Container |
| Language support | Any | Python, Node, Go, Java, etc. | Any |
| Scale to zero | Yes | Yes | No (min 1 node) |
| Startup time | Seconds | Milliseconds-seconds | N/A (always running) |
| Max timeout | 60 min (HTTP) | 60 min | No limit |
| Pricing | Per request + CPU/memory | Per invocation | Per node (always on) |
| Best for | Web apps, APIs, microservices | Event handlers, webhooks | Complex workloads, stateful apps |

### CI/CD Key Concepts

**Cloud Build Configuration (cloudbuild.yaml):**
```yaml
steps:
  # Build the Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'us-west1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA', '.']
  
  # Run tests
  - name: 'us-west1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
    entrypoint: 'python'
    args: ['-m', 'pytest', 'tests/']
  
  # Push to Artifact Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'us-west1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA']
  
  # Deploy to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    args:
      - 'gcloud'
      - 'run'
      - 'deploy'
      - 'my-app'
      - '--image=us-west1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
      - '--region=us-west1'
      - '--platform=managed'

images:
  - 'us-west1-docker.pkg.dev/$PROJECT_ID/my-repo/my-app:$COMMIT_SHA'
```

### Terraform Key Concepts

**Sample Terraform for GCP:**
```hcl
# Provider configuration
provider "google" {
  project = "my-info490-project"
  region  = "us-west1"
}

# Cloud Storage bucket
resource "google_storage_bucket" "data_bucket" {
  name     = "info490-data-bucket"
  location = "US-WEST1"
  
  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
  }
  
  versioning {
    enabled = true
  }
}

# Cloud Run service
resource "google_cloud_run_service" "web_app" {
  name     = "my-web-app"
  location = "us-west1"
  
  template {
    spec {
      containers {
        image = "us-west1-docker.pkg.dev/my-project/my-repo/my-app:latest"
        ports {
          container_port = 8080
        }
        resources {
          limits = {
            memory = "512Mi"
            cpu    = "1"
          }
        }
      }
    }
  }
}
```

---

## IMPORTANT DATES SUMMARY

| Date | Event |
|---|---|
| Week 1, Tuesday | First day of class; GCP credits distributed |
| Week 1, Thursday | Lab 1 assigned |
| Week 2, Thursday | Homework 1 assigned |
| Week 3, Tuesday | Lab 2 assigned; Teams formed for final project |
| Week 4, Thursday | **Homework 1 due**; Homework 2 assigned |
| Week 4, end | **Lab 1 due** |
| Week 5, Tuesday | Lab 3 assigned |
| Week 5, Thursday | **Final Project Proposal due** |
| Week 6, Thursday | **Homework 2 due**; Lab 4 assigned |
| Week 6, end | **Lab 2 due** |
| Week 7, Thursday | Homework 3 assigned |
| Week 7, end | **Lab 3 due** |
| Week 8, Tuesday | **MIDTERM EXAM** |
| Week 8, Thursday | Lab 5 assigned; Final Project Check-in (lab sections) |
| Week 8, end | **Lab 4 due** |
| Week 9, Thursday | **Homework 3 due**; Homework 4 assigned; Lab 6 assigned |
| Week 9, end | **Lab 5 due** |
| Week 10, Tuesday | **Homework 4 due**; Homework 5 assigned; Bonus Labs 7 & 8 assigned |
| Week 10, Thursday | **Final Project presentations**; **Final Project due (9 AM)** |
| Week 10, end | **Lab 6 due** |
| Finals Week, Tuesday | **Homework 5 due** |
| Finals Week, TBD | **Final Exam** |
| Finals Week, Friday | **Bonus Labs 7 & 8 due** |

---

## FREQUENTLY ASKED QUESTIONS

**Q: Do I need prior cloud computing experience for this course?**
A: No. The course starts with cloud fundamentals. However, you should be comfortable with basic programming (Python preferred), command-line interfaces, and web development concepts (HTTP, APIs, JSON). The prerequisites (INFO 340 or CSE 154) provide this foundation.

**Q: Will we use real GCP resources or simulators?**
A: Real GCP resources! Each student receives $300 in Google Cloud credits, which is more than enough for all coursework. You'll work in real GCP projects, deploy real applications, and manage real infrastructure.

**Q: What programming language is used in this course?**
A: Primarily Python, which is used for Cloud Functions, Vertex AI notebooks, BigQuery client libraries, and Terraform. Labs may also involve YAML (Kubernetes manifests, Cloud Build configs), SQL (BigQuery), HCL (Terraform), and basic shell scripting. JavaScript/HTML is needed only if your final project has a web frontend.

**Q: Can I use my personal GCP account?**
A: Please use the course-provided project and credits for all coursework. This ensures consistent environments, proper billing, and easier grading. You're welcome to experiment in personal projects on your own time.

**Q: How much does this course prepare me for Google Cloud certifications?**
A: The course covers approximately 80% of the topics on the Associate Cloud Engineer certification exam. After completing the course, you would need additional self-study (about 2-4 weeks) on topics like App Engine, Cloud SQL/Spanner, and Dataflow to be fully prepared. Dr. Chen will share a certification study guide in Week 10.

**Q: Is the final project individual or team-based?**
A: Team-based (3-4 students). Teams are formed in Week 3. Each team member is expected to contribute equitably, and peer evaluations are used to adjust individual grades if needed.

**Q: Can I attend a different lab section than the one I'm registered for?**
A: Yes, space permitting. Email your TA at least 24 hours in advance. However, you must attend a lab section each week to receive participation credit.

**Q: What if I run out of GCP credits?**
A: The $300 credit allocation is generous for coursework. If you run out due to accidental misconfiguration (e.g., leaving expensive VMs running), contact Dr. Chen or a TA. We can usually provide additional credits, but you should practice shutting down resources when not in use — this is itself an important cloud skill!

**Q: Are lectures recorded?**
A: Yes, lectures are recorded via Panopto and available on Canvas within 24 hours. However, in-class participation and lab quizzes require attendance.

**Q: How do I get help outside of office hours?**
A: Post on Piazza/Ed Discussion (monitored by TAs and Dr. Chen). For urgent issues (e.g., GCP access problems before a deadline), email the lead TA Marcus at mrivera.ta@uw.edu.

**Q: What happens if a GCP service goes down during a lab?**
A: GCP outages are rare but possible. If a service outage affects a lab or assignment deadline, we will extend the deadline. Check the Google Cloud Status Dashboard at status.cloud.google.com.

**Q: Can I work ahead on assignments?**
A: Yes! All assignment descriptions are posted in the syllabus. However, some labs require concepts from lectures that haven't happened yet, so working too far ahead may be challenging.

**Q: Is there extra credit available?**
A: Yes. Bonus Labs 7 (Terraform) and 8 (Security Audit) each offer 15 bonus points. Additionally, exceptional class participation, helping classmates on Piazza, or contributing to course improvement can earn up to 10 bonus participation points at Dr. Chen's discretion.

**Q: What IDE should I use?**
A: Visual Studio Code with the Cloud Code extension is recommended. It provides GCP integration, Kubernetes support, and Cloud Run deployment tools. However, you may use any IDE you're comfortable with. The Cloud Shell Editor (available in the GCP Console) is also an option if you prefer a browser-based environment.

---

## GOOGLE CLOUD SERVICES REFERENCE

This is a quick reference of all GCP services covered in this course:

### Compute
- **Compute Engine:** Virtual machines (IaaS)
- **Google Kubernetes Engine (GKE):** Managed Kubernetes
- **Cloud Run:** Serverless containers
- **Cloud Functions:** Serverless functions (FaaS)
- **App Engine:** Managed application platform (PaaS) — mentioned but not deeply covered

### Storage & Databases
- **Cloud Storage:** Object storage (buckets)
- **Cloud SQL:** Managed MySQL, PostgreSQL, SQL Server — mentioned in context of Cloud Run
- **Cloud Spanner:** Globally distributed relational database — mentioned briefly
- **Firestore:** NoSQL document database — mentioned briefly
- **Bigtable:** Wide-column NoSQL database — mentioned briefly
- **Memorystore:** Managed Redis and Memcached — mentioned in GKE lab

### Data Analytics
- **BigQuery:** Serverless data warehouse
- **Pub/Sub:** Messaging and event streaming
- **Dataflow:** Stream and batch data processing (Apache Beam) — mentioned briefly
- **Cloud Composer:** Managed Apache Airflow — mentioned briefly
- **Looker Studio:** Business intelligence and dashboards

### AI/ML
- **Vertex AI:** Unified ML platform (AutoML, custom training, notebooks, Feature Store, Model Registry)
- **Document AI:** Document processing — mentioned as final project example
- **Vision AI / Natural Language AI:** Pre-trained APIs — mentioned briefly

### DevOps & CI/CD
- **Cloud Build:** CI/CD pipelines
- **Artifact Registry:** Container and package repository
- **Cloud Deploy:** Managed continuous delivery
- **Cloud Source Repositories:** Git hosting (deprecated in favor of GitHub/GitLab)

### Networking
- **VPC:** Virtual Private Cloud
- **Cloud Load Balancing:** HTTP(S), TCP/SSL, Internal
- **Cloud CDN:** Content delivery network
- **Cloud Armor:** DDoS protection and WAF
- **Cloud DNS:** Domain name system
- **Cloud VPN / Interconnect:** Hybrid connectivity

### Security & Identity
- **Cloud IAM:** Identity and Access Management
- **Service Accounts:** Machine identities
- **Secret Manager:** Secure secret storage
- **Cloud KMS:** Key management service
- **Security Command Center:** Security and risk management
- **VPC Service Controls:** Data exfiltration protection
- **Cloud Audit Logs:** Activity logging

### Management & Monitoring
- **Cloud Monitoring:** Metrics, dashboards, alerting (formerly Stackdriver)
- **Cloud Logging:** Log management and analysis
- **Cloud Trace:** Distributed tracing
- **Cloud Profiler:** Application performance profiling
- **Billing:** Cost management, budgets, exports

### Infrastructure as Code
- **Terraform:** Third-party IaC tool with GCP provider
- **Deployment Manager:** GCP-native IaC (being replaced by Terraform)

---

## OFFICE HOURS SCHEDULE SUMMARY

| Day | Time | Person | Location |
|---|---|---|---|
| Monday | 3:00–5:00 PM | Marcus Rivera (TA) | CSE2 Room 153 |
| Tuesday | 1:00–2:30 PM | Dr. Sarah Chen | MGH Room 370E |
| Wednesday | 1:00–3:00 PM | Priya Patel (TA) | MGH Commons |
| Thursday | 2:00–3:00 PM | Dr. Sarah Chen | MGH Room 370E |
| By appointment | Email to schedule | Any instructor/TA | TBD |

---

## TIPS FOR SUCCESS IN THIS COURSE

1. **Start labs early.** GCP provisioning sometimes takes time, and you may encounter configuration issues. Don't wait until the night before the deadline.
2. **Always shut down resources after lab work.** Delete VMs, GKE clusters, and other running resources when you're done. This preserves your credits and is a critical cloud operations skill.
3. **Use the GCP documentation.** It's comprehensive and well-written. Get comfortable navigating it — you'll rely on it in your career.
4. **Practice with gcloud CLI.** The console is great for exploration, but the CLI is essential for automation, scripting, and certification exams.
5. **Attend office hours.** Even if you don't have a specific question, listening to others' questions often clarifies concepts.
6. **Form study groups.** Cloud computing has many services and concepts. Explaining them to peers helps reinforce your understanding.
7. **Keep your reference sheet for exams organized.** Focus on commands, service comparisons, and architecture patterns rather than trying to fit everything.
8. **Explore beyond the course.** GCP has 200+ services. We cover the core ones, but exploring others (like Dataflow, Cloud Composer, or AlloyDB) will deepen your understanding.
