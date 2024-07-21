import { createClient } from '@sanity/client';
import imageBuilder from '@sanity/image-url';

const client = createClient({
    projectId: 'uuqip568', // Replace with your actual project ID
    dataset: 'production', // Replace with your actual dataset name
    useCdn: true, // Use the CDN for faster, cacheable responses
    apiVersion: '2021-10-21', // Use a fixed API version date
});


const builder = imageBuilder(client);

export const urlFor = source=> builder.image(source);

export default client;

