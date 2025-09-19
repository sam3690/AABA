FROM node:20-alpine

WORKDIR /app

# Copy package.json and yarn.lock first for caching
COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

# Copy the rest of the app
COPY . .

# Build the app
RUN yarn build

EXPOSE 3000

# Run dev server (for local dev)
CMD ["yarn", "dev", "--host", "0.0.0.0"]
