export default{
    name: 'resturant',
    title: 'Restaurants',
    type: 'document',
    fields: [
        {
            name: 'name',
            type: 'string',
            title: 'Name',
            validation: rule=> rule.required(),
        },
        {
            name: 'description',
            type: 'string',
            title: 'Description',
            validation: rule=> rule.max(200),
        },
        {
            name: 'image',
            type: 'image',
            title: 'Image of the restaurant',
        },
        {
            name: 'lat',
            type: 'number',
            title: 'Latitude of the restaurant',
        },
        {
            name: 'lng',
            type: 'number',
            title: 'Longitude of the restaurant',
        },
        {
            name: 'address',
            type: 'string',
            title: 'Restaurant address',
            validation: rule=> rule.required(),
        },
        {
            name: 'rating',
            type: 'number',
            title: 'Rating',
            validation: rule=> rule.required().min(1).max(5).error('Pleaser enter a value between 1 to 5'),
        },
        {
            name: 'reviews',
            type: 'string',
            title: 'Reviews',
        },
        {
            name: 'type',
            type: 'reference',
            title: 'Category',
            validation: rule=> rule.required(),
            to: [{type: 'category'}]
        },
        {
            name: 'dishes',
            type: 'array',
            title: 'Dishes',
            of: [{type: 'reference', to:[{type: 'dish'}]}]
        },
    ]
}