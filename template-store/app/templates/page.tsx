"use client";

import { useEffect, useState } from "react";

export default function Home() {

  const [templates, setTemplates] = useState<any[]>([]);

  useEffect(() => {
    fetch("/api/templates")
      .then((res) => res.json())
      .then((data) => setTemplates(data));
  }, []);

  return (
    <main className="p-10">

      <h1 className="text-3xl font-bold mb-6">
        Video Templates
      </h1>

      <div className="grid grid-cols-3 gap-6">

        {templates.map((template) => (
          <div key={template._id} className="border p-4 rounded">

            <video controls width="250">
              <source src={template.video} type="video/mp4" />
            </video>

            <h2 className="text-xl mt-2">
              {template.title}
            </h2>

            <p className="text-green-600 font-bold">
              ₹{template.price}
            </p>

          </div>
        ))}

      </div>

    </main>
  );
}
