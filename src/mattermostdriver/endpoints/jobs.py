from .base import Base


class Jobs(Base):
    def get_jobs(self, params=None):
        """Get the jobs.

        page: The page to select.
        per_page: The number of jobs per page.
        """
        return self.client.get("""/jobs""", params=params)

    def create_job(self, options):
        """Create a new job.

        type: The type of job to create
        data: An object containing any additional data required for this job type
        """
        return self.client.post("""/jobs""", options=options)

    def get_job(self, job_id):
        """Get a job.

        job_id: Job GUID
        """
        return self.client.get(f"/jobs/{job_id}")

    def download_job(self, job_id):
        """Download the results of a job.

        job_id: Job GUID
        """
        return self.client.get(f"/jobs/{job_id}/download")

    def cancel_job(self, job_id):
        """Cancel a job.

        job_id: Job GUID
        """
        return self.client.post(f"/jobs/{job_id}/cancel")

    def get_jobs_by_type(self, type, params=None):
        """Get the jobs of the given type.

        type: Job type
        page: The page to select.
        per_page: The number of jobs per page.
        """
        return self.client.get(f"/jobs/type/{type}", params=params)
