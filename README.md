# XNL-21BPS1215-LLM-5
LLM Task 5: Intensive CI/CD Pipeline & Multi-Cloud Deployment for LLM-Powered Solutions

Overview
The project has an intense CI/CD pipeline to deploy an LLM-powered solution to multiple cloud providers (AWS & Azure). The pipeline provides automated testing, monitoring, and rollback processes to provide high availability and reliability.

Features
Continuous Integration (CI): Automated builds and testing using GitHub Actions.
Continuous Deployment (CD): Deployment to AWS & Azure.
Multi-Cloud Deployment: Provides redundancy and availability.
Observability & Monitoring: Bundled Prometheus & Grafana for real-time stats.
Automatic Rollback: Autosenses failures and rolls back to the last healthy version.

Steps for Deployment
1. Clone Repository

2. Configure CI/CD Pipeline

3. Build & Push Docker Image

i. Push to Azure Container Registry (ACR)

ii. Push to AWS Elastic Container Registry (ECR)

4. Deploy to Kubernetes (EKS & AKS)
i. Deploy on AWS (EKS)

ii. Deploy on Azure (AKS)

5. Install Monitoring with Prometheus & Grafana
i. Deploy Prometheus to gather statistics.

ii. Implement Grafana to graph logs and alerts.

6. Automatic Rollback Configuration
   Health checks check app performance. In case of a failed deployment, the last stable version 
   is automatically rolled back.
