
-- Churn rate by contract type
SELECT Contract, COUNT(*) as total_customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) as churned_customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) as churn_rate
FROM telco_churn
GROUP BY Contract;

-- Average monthly charges for churned vs retained
SELECT Churn, AVG(MonthlyCharges) as avg_monthly_charges
FROM telco_churn
GROUP BY Churn;
