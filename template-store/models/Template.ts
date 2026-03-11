import { Schema, model, models } from "mongoose";

const TemplateSchema = new Schema({
  title: String,
  price: Number,
  video: String,
  description: String
});

export default models.Template || model("Template", TemplateSchema);
