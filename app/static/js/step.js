class StepManager {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async fetchSteps(flowId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/flows/${flowId}/steps`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching steps:', error);
        }
    }

    async getStep(stepId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/steps/${stepId}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching step:', error);
        }
    }

    async createStep(stepData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/steps`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(stepData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating step:', error);
        }
    }

    async updateStep(stepId, stepData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/steps/${stepId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(stepData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating step:', error);
        }
    }

    async deleteStep(stepId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/steps/${stepId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting step:', error);
        }
    }
}

export default StepManager;
