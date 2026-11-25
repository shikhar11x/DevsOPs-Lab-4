# Q1: Automated Testing within a CI/CD Pipeline

## 1. Objective
To implement automated unit and integration testing within a Jenkins CI/CD pipeline and ensure that deployment is permitted only after successful testing.

## 2. Tools and Technologies
- Ubuntu 24.04 (WSL)
- Python 3.12.3
- Jenkins
- Git and GitHub
- Python unittest framework

## 3. Application Implementation
A Calculator application was developed with the following operations:
- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero exception handling

A separate CalculatorService class was implemented to integrate the calculator operations.

## 4. Automated Testing

### Unit Testing
Five unit test cases were implemented:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Division by zero

Result: 5/5 tests passed.

### Integration Testing
Five integration test cases were implemented:
1. Addition through CalculatorService
2. Multiplication through CalculatorService
3. Division through CalculatorService
4. Invalid operation handling
5. Division by zero handling

Result: 5/5 tests passed.

## 5. Jenkins CI/CD Pipeline

The Jenkins pipeline consists of:
1. Checkout
2. Environment Check
3. Unit Testing
4. Integration Testing
5. Deployment Gate

The pipeline automatically stops if a test command fails because Jenkins treats a non-zero shell exit code as a failed stage.

The Deployment Gate is a simulated approval stage. No production deployment was performed in this experiment.

## 6. Execution Results

Jenkins Job: Lab4-CI-CD-Testing

GitHub Repository:
https://github.com/shikhar11x/DevsOPs-Lab-4

Unit Tests: 5 passed
Integration Tests: 5 passed
Total Tests: 10 passed

Final Jenkins Build Status: SUCCESS

## 7. Observations
- Jenkins successfully fetched source code from GitHub.
- Python environment was detected successfully.
- All unit and integration tests executed automatically.
- The deployment gate was reached after successful testing.
- The pipeline completed without errors.

## 8. Advantages
- Early detection of software defects.
- Reduced manual testing effort.
- Consistent testing process.
- Faster feedback to developers.
- Prevents progression to the deployment gate when tests fail.

## 9. Limitations
- The calculator application is a demonstration project.
- Tests cover limited application functionality.
- Deployment approval is simulated, not a real production deployment.
- No code coverage or performance testing was configured.

## 10. Conclusion
Automated unit and integration testing was successfully implemented using Jenkins and Python unittest. The pipeline executed all 10 test cases successfully and reached the deployment gate. This demonstrates how automated testing improves software quality and reliability in CI/CD workflows.
