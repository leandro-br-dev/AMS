class ServiceManager {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async fetchServices() {
        try {
            const response = await fetch(`${this.baseUrl}/api/services`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching services:', error);
        }
    }

    async getService(serviceId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/services/${serviceId}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching service:', error);
        }
    }

    async createService(serviceData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/services`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(serviceData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating service:', error);
        }
    }

    async updateService(serviceId, serviceData) {
        try {
            const response = await fetch(`${this.baseUrl}/api/services/${serviceId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(serviceData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating service:', error);
        }
    }

    async deleteService(serviceId) {
        try {
            const response = await fetch(`${this.baseUrl}/api/services/${serviceId}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Error deleting service:', error);
        }
    }
}

export default ServiceManager;
