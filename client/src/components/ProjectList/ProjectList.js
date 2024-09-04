import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProjectList = () => {
  const [projects, setProjects] = useState([]); // State to hold the list of projects
  const [error, setError] = useState(null); // State to hold any error messages

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/projects/');
        console.log("Response")
        setProjects(response.data); // Set the projects state with the fetched data
      } catch (error) {
        console.error('Error fetching data:', error);
        setError('Failed to fetch projects'); // Set error message if the request fails
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>Project List</h1>
      {error && <p>{error}</p>} {/* Display error message if any */}
      <ul>
        {projects.map((project) => (
          <li key={project.id}>
            <h2>{project.title}</h2>
            <p>{project.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectList;